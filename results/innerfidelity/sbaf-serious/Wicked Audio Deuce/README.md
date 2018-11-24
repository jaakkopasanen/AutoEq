# Wicked Audio Deuce

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.6dB
GraphicEQ: 21 -13.9; 23 -13.8; 25 -13.7; 28 -13.6; 31 -13.4; 34 -13.2; 37 -13.1; 41 -12.9; 45 -12.7; 49 -12.5; 54 -12.4; 60 -12.2; 66 -12.0; 72 -11.9; 79 -11.8; 87 -11.7; 96 -11.6; 106 -11.2; 116 -10.9; 128 -10.6; 141 -10.3; 155 -9.8; 170 -9.3; 187 -8.8; 206 -8.3; 227 -7.6; 249 -7.1; 274 -6.4; 302 -5.7; 332 -5.1; 365 -4.3; 402 -3.7; 442 -2.9; 486 -2.4; 535 -1.8; 588 -1.0; 647 -0.5; 712 -0.3; 783 -0.1; 861 0.5; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.9; 1387 -1.1; 1526 -2.2; 1678 -3.3; 1846 -4.4; 2031 -5.1; 2234 -5.7; 2457 -5.5; 2703 -5.1; 2973 -3.2; 3270 -1.2; 3597 0.4; 3957 -0.3; 4353 -2.6; 4788 -4.7; 5267 -7.2; 5793 -12.6; 6373 -8.1; 7010 -3.8; 7711 -3.0; 8482 -5.2; 9330 -6.4; 10263 -2.7; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Wicked Audio Deuce GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-5**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Wicked Audio Deuce ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.17 | -13.5 dB |
| Peaking | 171 Hz   | 0.67 | -4.5 dB  |
| Peaking | 2226 Hz  | 2.38 | -5.9 dB  |
| Peaking | 5898 Hz  | 3.15 | -12.0 dB |
| Peaking | 22468 Hz | 2.24 | -3.8 dB  |
| Peaking | 853 Hz   | 2.06 | 1.4 dB   |
| Peaking | 1712 Hz  | 3.99 | -1.3 dB  |
| Peaking | 7157 Hz  | 5.86 | 1.4 dB   |
| Peaking | 8165 Hz  | 0.37 | 0.8 dB   |
| Peaking | 9141 Hz  | 4.02 | -6.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Wicked%20Audio%20Deuce/Wicked%20Audio%20Deuce.png)
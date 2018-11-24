# Audio Technica ATH-M70x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 21 -0.7; 23 -1.2; 25 -1.6; 28 -2.0; 31 -2.4; 34 -2.6; 37 -2.7; 41 -2.8; 45 -2.7; 49 -2.3; 54 -1.6; 60 -0.9; 66 -0.3; 72 0.9; 79 2.5; 87 3.7; 96 2.8; 106 0.0; 116 -1.9; 128 -1.7; 141 0.1; 155 1.5; 170 1.4; 187 -0.8; 206 0.1; 227 0.2; 249 0.2; 274 0.4; 302 0.7; 332 0.9; 365 1.2; 402 1.4; 442 1.7; 486 1.8; 535 2.1; 588 2.8; 647 3.7; 712 2.4; 783 1.6; 861 0.7; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.7; 1387 -1.4; 1526 -2.3; 1678 -3.2; 1846 -3.6; 2031 -3.5; 2234 -2.8; 2457 -1.3; 2703 0.6; 2973 1.3; 3270 0.3; 3597 -0.5; 3957 -1.1; 4353 -4.2; 4788 -3.8; 5267 -1.1; 5793 3.0; 6373 4.0; 7010 2.4; 7711 -0.7; 8482 -4.1; 9330 -5.6; 10263 -3.7; 11289 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M70x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M70x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 87 Hz    | 6.99 | 4.3 dB   |
| Peaking | 1817 Hz  | 0.99 | -9.3 dB  |
| Peaking | 4659 Hz  | 2.37 | -11.4 dB |
| Peaking | 6623 Hz  | 0.36 | 30.3 dB  |
| Peaking | 8576 Hz  | 0.54 | -29.2 dB |
| Peaking | 38 Hz    | 1.49 | -3.1 dB  |
| Peaking | 234 Hz   | 2.11 | -0.5 dB  |
| Peaking | 635 Hz   | 4.38 | 1.9 dB   |
| Peaking | 926 Hz   | 3.6  | -1.2 dB  |
| Peaking | 11363 Hz | 7.46 | 2.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-M70x/Audio%20Technica%20ATH-M70x.png)
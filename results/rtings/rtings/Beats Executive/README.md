# Beats Executive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.8; 28 4.5; 31 2.5; 34 0.8; 37 -0.6; 41 -2.3; 45 -3.6; 49 -4.8; 54 -6.1; 60 -7.3; 66 -8.4; 72 -9.2; 79 -10.1; 87 -11.0; 96 -11.8; 106 -12.5; 116 -13.1; 128 -13.6; 141 -13.9; 155 -14.0; 170 -14.0; 187 -13.7; 206 -13.2; 227 -12.4; 249 -11.3; 274 -9.8; 302 -8.0; 332 -6.0; 365 -3.8; 402 -2.1; 442 -1.4; 486 -1.8; 535 -1.5; 588 -1.2; 647 -1.2; 712 -1.1; 783 -0.5; 861 0.8; 947 0.4; 1042 -0.4; 1146 -1.6; 1261 -1.8; 1387 -3.5; 1526 -4.6; 1678 -5.3; 1846 -6.9; 2031 -7.9; 2234 -8.4; 2457 -8.6; 2703 -8.6; 2973 -9.4; 3270 -12.7; 3597 -9.5; 3957 -3.5; 4353 -4.5; 4788 -7.4; 5267 -3.8; 5793 -2.4; 6373 -4.3; 7010 -4.6; 7711 -7.0; 8482 -9.2; 9330 -10.9; 10263 -10.3; 11289 -5.9; 12418 -2.8; 13660 -5.4; 15026 -9.6; 16529 -8.3; 18182 -2.7; 20000 -0.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Executive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Executive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 143 Hz   | 0.7  | -15.2 dB |
| Peaking | 2867 Hz  | 1.19 | -10.3 dB |
| Peaking | 9373 Hz  | 2.29 | -10.4 dB |
| Peaking | 15732 Hz | 2.27 | -10.0 dB |
| Peaking | 24000 Hz | 1.97 | -7.2 dB  |
| Peaking | 23 Hz    | 1.45 | 7.9 dB   |
| Peaking | 62 Hz    | 1.84 | -2.8 dB  |
| Peaking | 254 Hz   | 2.66 | -3.3 dB  |
| Peaking | 431 Hz   | 1.9  | 2.9 dB   |
| Peaking | 900 Hz   | 4.09 | 2.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Beats%20Executive/Beats%20Executive.png)
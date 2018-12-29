# Sennheiser HD 598 SR

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.5; 31 4.8; 34 4.2; 37 3.6; 41 3.0; 45 2.4; 49 1.9; 54 1.3; 60 0.7; 66 0.2; 72 -0.3; 79 -0.5; 87 -0.7; 96 -0.8; 106 -1.8; 116 -2.8; 128 -3.3; 141 -3.7; 155 -4.0; 170 -4.1; 187 -4.1; 206 -4.1; 227 -3.9; 249 -3.7; 274 -3.4; 302 -3.1; 332 -2.7; 365 -2.3; 402 -2.0; 442 -1.9; 486 -1.8; 535 -1.4; 588 -1.0; 647 -0.8; 712 0.7; 783 0.1; 861 -0.4; 947 -0.1; 1042 -0.0; 1146 0.2; 1261 0.2; 1387 0.8; 1526 2.0; 1678 2.6; 1846 2.6; 2031 1.9; 2234 1.7; 2457 1.7; 2703 0.2; 2973 -1.4; 3270 -2.4; 3597 -1.1; 3957 -0.1; 4353 -1.5; 4788 -1.4; 5267 -2.2; 5793 -3.1; 6373 1.6; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.1; 16529 -3.6; 18182 -5.0; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 SR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 SR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.67 | 6.2 dB  |
| Peaking | 189 Hz   | 0.65 | -4.5 dB |
| Peaking | 1872 Hz  | 1.67 | 2.9 dB  |
| Peaking | 3220 Hz  | 4.39 | -3.0 dB |
| Peaking | 5519 Hz  | 7.42 | -3.5 dB |
| Peaking | 96 Hz    | 6.69 | 0.9 dB  |
| Peaking | 716 Hz   | 1.32 | -0.6 dB |
| Peaking | 728 Hz   | 5.79 | 1.8 dB  |
| Peaking | 6777 Hz  | 9.55 | 4.3 dB  |
| Peaking | 19721 Hz | 1.16 | -7.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20598%20SR/Sennheiser%20HD%20598%20SR.png)
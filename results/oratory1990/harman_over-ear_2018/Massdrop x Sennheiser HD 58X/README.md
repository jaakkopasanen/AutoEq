# Massdrop x Sennheiser HD 58X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.2; 87 3.9; 96 3.0; 106 2.2; 116 1.4; 128 0.6; 141 -0.2; 155 -0.7; 170 -0.9; 187 -1.4; 206 -1.6; 227 -1.6; 249 -1.5; 274 -1.3; 302 -1.1; 332 -0.7; 365 -0.4; 402 -0.2; 442 0.0; 486 0.1; 535 0.3; 588 0.6; 647 0.6; 712 0.5; 783 0.5; 861 0.6; 947 0.6; 1042 -0.3; 1146 -0.6; 1261 -0.3; 1387 0.2; 1526 1.0; 1678 1.7; 1846 2.7; 2031 3.6; 2234 4.0; 2457 4.3; 2703 3.7; 2973 2.7; 3270 1.8; 3597 1.6; 3957 2.3; 4353 4.0; 4788 1.9; 5267 -1.7; 5793 -0.7; 6373 4.7; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -2.0; 20000 -10.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Sennheiser HD 58X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Sennheiser HD 58X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 68 Hz   | 0.22 | 8.0 dB  |
| Peaking | 177 Hz  | 0.64 | -7.8 dB |
| Peaking | 2368 Hz | 2.11 | 4.6 dB  |
| Peaking | 4371 Hz | 7.9  | 3.8 dB  |
| Peaking | 6561 Hz | 9.57 | 5.0 dB  |
| Peaking | 67 Hz   | 0.97 | -0.7 dB |
| Peaking | 74 Hz   | 3.46 | 1.5 dB  |
| Peaking | 287 Hz  | 2.35 | -0.2 dB |
| Peaking | 1176 Hz | 4.14 | -1.0 dB |
| Peaking | 5483 Hz | 5.48 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Sennheiser%20HD%2058X/Massdrop%20x%20Sennheiser%20HD%2058X.png)
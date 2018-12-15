# Sennheiser HD 598 SR

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.6; 66 4.9; 72 4.2; 79 3.6; 87 3.1; 96 2.5; 106 1.1; 116 -0.5; 128 -1.4; 141 -2.3; 155 -3.0; 170 -3.5; 187 -3.8; 206 -4.0; 227 -4.0; 249 -3.7; 274 -3.4; 302 -3.1; 332 -2.7; 365 -2.3; 402 -2.0; 442 -1.9; 486 -1.8; 535 -1.4; 588 -1.0; 647 -0.8; 712 0.7; 783 0.1; 861 -0.4; 947 -0.1; 1042 -0.0; 1146 0.2; 1261 0.2; 1387 0.8; 1526 2.0; 1678 2.6; 1846 2.6; 2031 1.9; 2234 1.7; 2457 1.7; 2703 0.2; 2973 -1.4; 3270 -2.4; 3597 -1.1; 3957 -0.1; 4353 -1.5; 4788 -1.4; 5267 -2.2; 5793 -3.1; 6373 1.6; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.1; 16529 -3.6; 18182 -5.0; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 SR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 SR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 53 Hz    | 0.28 | 7.7 dB  |
| Peaking | 177 Hz   | 0.63 | -8.2 dB |
| Peaking | 1874 Hz  | 1.63 | 2.9 dB  |
| Peaking | 3223 Hz  | 4.35 | -3.0 dB |
| Peaking | 5510 Hz  | 7.58 | -3.5 dB |
| Peaking | 476 Hz   | 6.17 | -0.4 dB |
| Peaking | 727 Hz   | 7.15 | 1.6 dB  |
| Peaking | 828 Hz   | 1.08 | -0.3 dB |
| Peaking | 6758 Hz  | 9.57 | 4.3 dB  |
| Peaking | 19727 Hz | 1.16 | -7.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20598%20SR/Sennheiser%20HD%20598%20SR.png)
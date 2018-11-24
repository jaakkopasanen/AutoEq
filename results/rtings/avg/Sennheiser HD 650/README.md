# Sennheiser HD 650

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.5; 37 5.0; 41 4.4; 45 4.0; 49 3.6; 54 3.1; 60 2.5; 66 2.0; 72 1.5; 79 1.0; 87 0.4; 96 -0.1; 106 -0.6; 116 -1.1; 128 -1.5; 141 -1.8; 155 -2.0; 170 -2.1; 187 -2.2; 206 -2.0; 227 -1.9; 249 -1.7; 274 -1.7; 302 -1.6; 332 -1.6; 365 -1.5; 402 -1.5; 442 -1.5; 486 -1.4; 535 -1.4; 588 -1.2; 647 -1.1; 712 -0.9; 783 -0.9; 861 -0.8; 947 -0.2; 1042 -0.4; 1146 -0.7; 1261 -1.1; 1387 -1.4; 1526 -1.6; 1678 -1.8; 1846 -2.0; 2031 -2.2; 2234 -1.5; 2457 -1.2; 2703 -1.2; 2973 -1.7; 3270 -1.9; 3597 -1.6; 3957 -0.8; 4353 -0.1; 4788 -0.3; 5267 0.0; 5793 1.2; 6373 2.3; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.7; 16529 -0.5; 18182 -1.5; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.36 | 6.6 dB  |
| Peaking | 144 Hz   | 0.38 | -3.1 dB |
| Peaking | 1835 Hz  | 1.74 | -1.9 dB |
| Peaking | 3304 Hz  | 3.39 | -1.7 dB |
| Peaking | 6603 Hz  | 5.29 | 3.2 dB  |
| Peaking | 166 Hz   | 1.34 | -0.9 dB |
| Peaking | 236 Hz   | 0.68 | 0.9 dB  |
| Peaking | 487 Hz   | 0.82 | -0.6 dB |
| Peaking | 988 Hz   | 8.48 | 0.8 dB  |
| Peaking | 20029 Hz | 1.78 | -4.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20650/Sennheiser%20HD%20650.png)
# Phiaton PS 200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.6; 25 1.5; 28 1.5; 31 1.4; 34 1.2; 37 1.1; 41 1.0; 45 0.9; 49 0.7; 54 0.5; 60 0.2; 66 -0.1; 72 -0.4; 79 -0.7; 87 -1.0; 96 -1.3; 106 -1.5; 116 -1.8; 128 -2.1; 141 -2.3; 155 -2.4; 170 -2.6; 187 -2.7; 206 -2.8; 227 -2.6; 249 -2.6; 274 -2.5; 302 -2.3; 332 -2.0; 365 -1.7; 402 -1.4; 442 -1.2; 486 -0.9; 535 -0.6; 588 -0.3; 647 0.1; 712 0.3; 783 0.4; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.7; 1387 -1.2; 1526 -1.6; 1678 -1.8; 1846 -1.6; 2031 -1.1; 2234 -0.3; 2457 1.1; 2703 3.4; 2973 5.9; 3270 6.0; 3597 6.0; 3957 6.0; 4353 4.5; 4788 3.3; 5267 3.1; 5793 2.1; 6373 0.3; 7010 -1.5; 7711 -2.9; 8482 -4.5; 9330 -7.1; 10263 -6.9; 11289 -1.0; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.67 | 1.7 dB  |
| Peaking | 192 Hz   | 0.7  | -2.9 dB |
| Peaking | 2020 Hz  | 1.5  | -4.8 dB |
| Peaking | 3325 Hz  | 1.12 | 7.9 dB  |
| Peaking | 9385 Hz  | 2.66 | -8.4 dB |
| Peaking | 794 Hz   | 2.74 | 0.9 dB  |
| Peaking | 1457 Hz  | 5.1  | -0.6 dB |
| Peaking | 5574 Hz  | 7.05 | 0.9 dB  |
| Peaking | 7124 Hz  | 4.79 | -1.3 dB |
| Peaking | 11979 Hz | 5.9  | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20PS%20200/Phiaton%20PS%20200.png)
# Phiaton PS 320

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.0; 25 3.0; 28 3.2; 31 3.3; 34 3.1; 37 2.8; 41 2.7; 45 2.6; 49 2.3; 54 2.3; 60 3.1; 66 3.7; 72 2.3; 79 1.1; 87 0.3; 96 -0.3; 106 -0.7; 116 -0.5; 128 -0.3; 141 0.1; 155 0.9; 170 -0.9; 187 -2.3; 206 -3.0; 227 -3.1; 249 -3.9; 274 -4.4; 302 -4.0; 332 -3.6; 365 -2.4; 402 -1.1; 442 -0.5; 486 0.3; 535 1.5; 588 2.3; 647 2.8; 712 2.6; 783 2.2; 861 1.8; 947 0.9; 1042 -0.7; 1146 -1.6; 1261 -1.9; 1387 -2.7; 1526 -3.4; 1678 -3.9; 1846 -4.1; 2031 -4.3; 2234 -4.5; 2457 -3.0; 2703 -1.0; 2973 0.7; 3270 1.6; 3597 2.2; 3957 2.9; 4353 4.7; 4788 6.0; 5267 6.0; 5793 5.2; 6373 -0.2; 7010 -0.6; 7711 -0.6; 8482 -2.5; 9330 -1.6; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -3.2; 16529 -4.9; 18182 -4.6; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 320 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 320 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.91 | 3.5 dB  |
| Peaking | 64 Hz    | 4.71 | 3.1 dB  |
| Peaking | 266 Hz   | 2.22 | -4.8 dB |
| Peaking | 1942 Hz  | 2.06 | -5.2 dB |
| Peaking | 4803 Hz  | 2.72 | 7.0 dB  |
| Peaking | 351 Hz   | 3.54 | -1.6 dB |
| Peaking | 703 Hz   | 1.53 | 3.5 dB  |
| Peaking | 1244 Hz  | 2.02 | -1.8 dB |
| Peaking | 3254 Hz  | 5.27 | 1.6 dB  |
| Peaking | 19725 Hz | 0.64 | -6.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20PS%20320/Phiaton%20PS%20320.png)
# AKG K81 DJ

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 5.8; 170 5.5; 187 5.5; 206 5.6; 227 5.9; 249 5.5; 274 4.8; 302 3.9; 332 2.7; 365 1.3; 402 0.0; 442 -0.3; 486 -0.1; 535 0.1; 588 0.0; 647 0.4; 712 0.5; 783 0.5; 861 0.5; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.5; 1387 -1.0; 1526 -1.7; 1678 -1.6; 1846 -1.3; 2031 -1.2; 2234 -1.6; 2457 -0.0; 2703 1.3; 2973 2.7; 3270 3.8; 3597 3.2; 3957 1.2; 4353 -0.0; 4788 1.7; 5267 5.2; 5793 3.1; 6373 -1.4; 7010 -1.5; 7711 0.0; 8482 0.0; 9330 -0.9; 10263 -0.2; 11289 0.0; 12418 0.0; 13660 -0.4; 15026 -5.8; 16529 -5.6; 18182 -2.8; 20000 -2.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K81 DJ GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K81 DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 69 Hz    | 0.17 | 6.5 dB  |
| Peaking | 4079 Hz  | 0.85 | 5.2 dB  |
| Peaking | 4353 Hz  | 0.08 | -2.6 dB |
| Peaking | 13338 Hz | 1.52 | 5.5 dB  |
| Peaking | 15384 Hz | 1.75 | -7.5 dB |
| Peaking | 427 Hz   | 4.97 | -2.4 dB |
| Peaking | 3330 Hz  | 4.65 | 3.1 dB  |
| Peaking | 4405 Hz  | 2.49 | -3.9 dB |
| Peaking | 5422 Hz  | 4.76 | 6.4 dB  |
| Peaking | 6484 Hz  | 6.12 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K81%20DJ/AKG%20K81%20DJ.png)
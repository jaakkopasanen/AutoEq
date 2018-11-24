# AKG K271 MKII

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.8; 87 4.7; 96 3.8; 106 2.9; 116 2.2; 128 1.4; 141 0.6; 155 0.1; 170 0.5; 187 0.1; 206 -0.3; 227 0.1; 249 -0.1; 274 0.2; 302 -0.2; 332 -0.6; 365 -0.6; 402 -0.8; 442 -1.2; 486 -1.5; 535 -1.6; 588 -2.0; 647 -3.3; 712 -0.2; 783 1.1; 861 0.9; 947 0.6; 1042 -0.4; 1146 -1.0; 1261 -1.5; 1387 -2.4; 1526 -3.0; 1678 -3.2; 1846 -2.6; 2031 -0.2; 2234 2.0; 2457 0.3; 2703 -0.1; 2973 0.2; 3270 2.6; 3597 3.2; 3957 2.2; 4353 0.6; 4788 2.2; 5267 4.7; 5793 5.6; 6373 4.5; 7010 2.2; 7711 -3.8; 8482 -8.0; 9330 -8.3; 10263 -4.8; 11289 -0.3; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K271 MKII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K271 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 41 Hz   | 0.58 | 7.0 dB   |
| Peaking | 1565 Hz | 3    | -3.6 dB  |
| Peaking | 3446 Hz | 5.64 | 3.2 dB   |
| Peaking | 6055 Hz | 2.42 | 7.3 dB   |
| Peaking | 8816 Hz | 3    | -10.9 dB |
| Peaking | 21 Hz   | 3.09 | 1.9 dB   |
| Peaking | 78 Hz   | 4.94 | 2.0 dB   |
| Peaking | 716 Hz  | 1.51 | -5.2 dB  |
| Peaking | 744 Hz  | 9.03 | 3.5 dB   |
| Peaking | 848 Hz  | 2.36 | 4.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K271%20MKII/AKG%20K271%20MKII.png)
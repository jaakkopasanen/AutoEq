# Shure SRH750DJ

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 -3.6; 23 -4.1; 25 -4.5; 28 -5.1; 31 -5.5; 34 -5.9; 37 -6.1; 41 -6.4; 45 -6.6; 49 -6.7; 54 -6.6; 60 -6.7; 66 -7.0; 72 -7.5; 79 -7.4; 87 -6.8; 96 -5.3; 106 -4.3; 116 -4.7; 128 -6.2; 141 -7.1; 155 -7.1; 170 -5.7; 187 -6.4; 206 -5.6; 227 -4.7; 249 -4.9; 274 -3.7; 302 -2.4; 332 -1.3; 365 -0.6; 402 -0.3; 442 -0.4; 486 -0.6; 535 -0.7; 588 -0.7; 647 -0.7; 712 -0.5; 783 -0.1; 861 0.5; 947 0.6; 1042 -0.4; 1146 -0.5; 1261 -0.4; 1387 -1.3; 1526 -2.6; 1678 -4.4; 1846 -6.3; 2031 -7.8; 2234 -8.0; 2457 -6.0; 2703 -3.2; 2973 -0.9; 3270 0.7; 3597 1.0; 3957 -0.3; 4353 -4.0; 4788 -1.0; 5267 0.9; 5793 4.2; 6373 5.5; 7010 2.5; 7711 -0.7; 8482 -5.6; 9330 -6.9; 10263 -4.0; 11289 -0.1; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH750DJ GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH750DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 0.51 | -6.9 dB |
| Peaking | 180 Hz  | 1.36 | -4.7 dB |
| Peaking | 2105 Hz | 2.73 | -8.8 dB |
| Peaking | 6336 Hz | 4.63 | 7.2 dB  |
| Peaking | 9114 Hz | 3.77 | -8.1 dB |
| Peaking | 15 Hz   | 1.4  | -0.6 dB |
| Peaking | 391 Hz  | 5.05 | 1.1 dB  |
| Peaking | 910 Hz  | 5.14 | 1.3 dB  |
| Peaking | 3481 Hz | 4.55 | 2.5 dB  |
| Peaking | 4402 Hz | 8.18 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH750DJ/Shure%20SRH750DJ.png)
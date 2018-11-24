# Logitech G430

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 21 0.0; 23 0.7; 25 -0.1; 28 -1.2; 31 -2.1; 34 -2.8; 37 -3.4; 41 -3.9; 45 -4.3; 49 -4.5; 54 -4.6; 60 -4.6; 66 -4.5; 72 -4.3; 79 -4.2; 87 -4.4; 96 -4.6; 106 -4.9; 116 -4.9; 128 -4.6; 141 -4.5; 155 -4.3; 170 -3.9; 187 -3.5; 206 -3.1; 227 -2.6; 249 -2.7; 274 -2.4; 302 -1.3; 332 -0.6; 365 0.2; 402 1.0; 442 1.6; 486 1.3; 535 0.3; 588 -0.4; 647 -0.5; 712 -0.5; 783 -0.4; 861 -0.3; 947 -0.2; 1042 0.1; 1146 -0.0; 1261 0.3; 1387 0.6; 1526 -0.3; 1678 -0.5; 1846 -1.0; 2031 -1.1; 2234 -0.1; 2457 1.7; 2703 3.0; 2973 3.4; 3270 3.9; 3597 5.1; 3957 4.6; 4353 0.7; 4788 0.3; 5267 1.1; 5793 -0.1; 6373 -2.9; 7010 1.7; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -1.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G430 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G430 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  1.45 | 4.8 dB  |
| Peaking | 72 Hz   |  0.25 | -5.0 dB |
| Peaking | 424 Hz  |  2.23 | 3.2 dB  |
| Peaking | 1955 Hz |  5.09 | -1.8 dB |
| Peaking | 3417 Hz |  2.49 | 5.2 dB  |
| Peaking | 80 Hz   |  5.46 | 0.5 dB  |
| Peaking | 1328 Hz |  9.38 | 0.8 dB  |
| Peaking | 2671 Hz |  9.61 | 1.2 dB  |
| Peaking | 6357 Hz |  9.02 | -4.0 dB |
| Peaking | 7073 Hz | 10.73 | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Logitech%20G430/Logitech%20G430.png)
# Logitech G433

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 0.0; 23 0.8; 25 0.4; 28 -0.2; 31 -0.6; 34 -1.1; 37 -1.4; 41 -1.7; 45 -1.9; 49 -1.9; 54 -1.9; 60 -1.9; 66 -2.0; 72 -2.0; 79 -2.1; 87 -2.4; 96 -2.9; 106 -3.6; 116 -4.3; 128 -4.7; 141 -4.7; 155 -4.8; 170 -4.7; 187 -4.4; 206 -3.7; 227 -3.0; 249 -2.4; 274 -1.6; 302 -0.8; 332 -0.1; 365 0.4; 402 0.4; 442 -0.2; 486 -1.1; 535 -2.1; 588 -3.1; 647 -3.7; 712 -3.7; 783 -2.8; 861 -1.5; 947 -0.3; 1042 0.1; 1146 -0.0; 1261 -0.2; 1387 -0.4; 1526 -0.0; 1678 0.2; 1846 -0.4; 2031 -1.2; 2234 -1.1; 2457 -0.0; 2703 0.6; 2973 1.0; 3270 1.2; 3597 -0.6; 3957 -4.2; 4353 -3.6; 4788 -0.7; 5267 1.2; 5793 5.0; 6373 4.9; 7010 1.5; 7711 -1.3; 8482 -3.6; 9330 -5.3; 10263 -3.8; 11289 -0.2; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G433 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G433 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 141 Hz  | 0.98 | -5.0 dB |
| Peaking | 675 Hz  | 3.36 | -4.0 dB |
| Peaking | 4163 Hz | 6.33 | -5.4 dB |
| Peaking | 6100 Hz | 4.49 | 6.8 dB  |
| Peaking | 9250 Hz | 3.37 | -6.0 dB |
| Peaking | 16 Hz   | 1.18 | 2.3 dB  |
| Peaking | 42 Hz   | 1.66 | -1.6 dB |
| Peaking | 372 Hz  | 4.37 | 1.8 dB  |
| Peaking | 2121 Hz | 6.45 | -1.4 dB |
| Peaking | 3100 Hz | 4.98 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Logitech%20G433/Logitech%20G433.png)
# Logitech G930

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.7; 25 2.1; 28 1.4; 31 0.9; 34 0.7; 37 0.6; 41 0.6; 45 0.7; 49 0.8; 54 1.0; 60 1.4; 66 1.6; 72 1.6; 79 1.4; 87 1.0; 96 0.6; 106 0.2; 116 0.0; 128 0.0; 141 0.3; 155 0.8; 170 1.6; 187 2.6; 206 3.9; 227 5.8; 249 6.0; 274 6.0; 302 6.0; 332 4.7; 365 2.9; 402 1.8; 442 1.3; 486 0.8; 535 0.4; 588 0.2; 647 0.1; 712 0.0; 783 -0.2; 861 -0.3; 947 -0.2; 1042 0.2; 1146 1.1; 1261 1.9; 1387 2.5; 1526 1.5; 1678 1.1; 1846 1.6; 2031 2.4; 2234 3.3; 2457 4.5; 2703 5.9; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 1.4; 4788 -0.2; 5267 3.4; 5793 4.6; 6373 0.4; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G930 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G930 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 266 Hz   | 1.91 | 6.7 dB  |
| Peaking | 2727 Hz  | 2.25 | 0.9 dB  |
| Peaking | 3230 Hz  | 1.29 | 5.7 dB  |
| Peaking | 24000 Hz | 2.42 | 1.3 dB  |
| Peaking | 18 Hz    | 1.71 | 3.5 dB  |
| Peaking | 67 Hz    | 3.15 | 1.5 dB  |
| Peaking | 4077 Hz  | 6.14 | 4.3 dB  |
| Peaking | 4531 Hz  | 4.06 | -5.5 dB |
| Peaking | 5570 Hz  | 6.24 | 4.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Logitech%20G930/Logitech%20G930.png)
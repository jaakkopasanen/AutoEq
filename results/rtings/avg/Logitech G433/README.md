# Logitech G433

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 21 0.0; 23 0.8; 25 0.4; 28 -0.2; 31 -0.6; 34 -1.1; 37 -1.4; 41 -1.7; 45 -1.9; 49 -1.9; 54 -1.9; 60 -1.9; 66 -2.0; 72 -2.0; 79 -2.1; 87 -2.4; 96 -2.9; 106 -3.6; 116 -4.3; 128 -4.7; 141 -4.7; 155 -4.8; 170 -4.7; 187 -4.4; 206 -3.7; 227 -3.0; 249 -2.4; 274 -1.6; 302 -0.8; 332 -0.1; 365 0.4; 402 0.4; 442 -0.2; 486 -1.1; 535 -2.1; 588 -3.1; 647 -3.7; 712 -3.7; 783 -2.8; 861 -1.5; 947 -0.3; 1042 0.1; 1146 -0.0; 1261 -0.2; 1387 -0.4; 1526 -0.0; 1678 0.2; 1846 -0.4; 2031 -1.2; 2234 -1.1; 2457 -0.1; 2703 0.3; 2973 0.5; 3270 0.5; 3597 -1.6; 3957 -5.5; 4353 -4.9; 4788 -2.5; 5267 -1.4; 5793 2.5; 6373 3.7; 7010 0.8; 7711 -1.7; 8482 -2.7; 9330 -2.6; 10263 -1.6; 11289 -0.6; 12418 -0.6; 13660 -1.1; 15026 -2.0; 16529 -2.7; 18182 -3.3; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G433 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-43**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G433 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 141 Hz   | 0.98 | -5.0 dB |
| Peaking | 674 Hz   | 3.38 | -4.0 dB |
| Peaking | 4184 Hz  | 4.85 | -6.1 dB |
| Peaking | 6187 Hz  | 7.33 | 5.5 dB  |
| Peaking | 21739 Hz | 0.19 | -4.1 dB |
| Peaking | 16 Hz    | 1.17 | 2.1 dB  |
| Peaking | 42 Hz    | 1.73 | -1.7 dB |
| Peaking | 371 Hz   | 4.4  | 1.8 dB  |
| Peaking | 8967 Hz  | 2.42 | -4.2 dB |
| Peaking | 10223 Hz | 1    | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G433/Logitech%20G433.png)
# Panasonic RP-HC200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 5.7; 116 5.1; 128 4.6; 141 4.5; 155 4.4; 170 4.4; 187 4.3; 206 4.6; 227 4.6; 249 4.7; 274 4.7; 302 5.2; 332 5.6; 365 5.6; 402 5.6; 442 5.4; 486 4.9; 535 4.1; 588 3.0; 647 1.7; 712 0.6; 783 -0.2; 861 -0.6; 947 -0.0; 1042 0.1; 1146 0.5; 1261 1.7; 1387 1.7; 1526 2.3; 1678 3.6; 1846 5.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.9; 6373 4.7; 7010 2.5; 7711 0.3; 8482 -2.9; 9330 -0.2; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -1.6; 15026 -4.9; 16529 -2.2; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 43 Hz    | 0.2  | 6.2 dB  |
| Peaking | 381 Hz   | 1.7  | 4.5 dB  |
| Peaking | 3911 Hz  | 0.63 | 7.7 dB  |
| Peaking | 11915 Hz | 0.46 | -3.0 dB |
| Peaking | 24000 Hz | 1.55 | -2.6 dB |
| Peaking | 906 Hz   | 2.52 | -2.3 dB |
| Peaking | 2087 Hz  | 2.84 | 2.5 dB  |
| Peaking | 6237 Hz  | 1.77 | 6.6 dB  |
| Peaking | 8399 Hz  | 0.73 | -7.7 dB |
| Peaking | 10957 Hz | 1.63 | 7.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HC200/Panasonic%20RP-HC200.png)
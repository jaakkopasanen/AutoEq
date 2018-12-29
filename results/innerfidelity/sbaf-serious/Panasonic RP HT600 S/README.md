# Panasonic RP HT600 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.9; 25 -0.1; 28 -1.4; 31 -2.3; 34 -3.0; 37 -3.5; 41 -3.9; 45 -4.0; 49 -4.1; 54 -4.2; 60 -4.1; 66 -4.1; 72 -4.1; 79 -4.2; 87 -4.2; 96 -4.4; 106 -4.3; 116 -4.0; 128 -4.3; 141 -4.6; 155 -4.9; 170 -4.7; 187 -4.8; 206 -5.0; 227 -5.0; 249 -5.1; 274 -5.2; 302 -5.3; 332 -5.2; 365 -5.3; 402 -5.3; 442 -5.2; 486 -5.3; 535 -5.4; 588 -4.9; 647 -4.5; 712 -4.1; 783 -3.4; 861 -2.2; 947 -0.5; 1042 0.1; 1146 0.1; 1261 -1.4; 1387 -3.9; 1526 -6.0; 1678 -6.4; 1846 -5.8; 2031 -3.4; 2234 -1.8; 2457 -0.1; 2703 1.7; 2973 3.2; 3270 3.9; 3597 3.7; 3957 5.8; 4353 5.4; 4788 3.3; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -3.6; 9330 -6.7; 10263 -1.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP HT600 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP HT600 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 189 Hz  | 0.23 | -5.2 dB |
| Peaking | 1747 Hz | 3.12 | -6.9 dB |
| Peaking | 3798 Hz | 1.29 | 4.9 dB  |
| Peaking | 5992 Hz | 2.84 | 5.0 dB  |
| Peaking | 9133 Hz | 4.99 | -8.3 dB |
| Peaking | 17 Hz   | 0.19 | 6.3 dB  |
| Peaking | 39 Hz   | 0.69 | -6.8 dB |
| Peaking | 756 Hz  | 0.81 | -2.5 dB |
| Peaking | 1048 Hz | 1.85 | 4.8 dB  |
| Peaking | 1452 Hz | 5.83 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Panasonic%20RP%20HT600%20S/Panasonic%20RP%20HT600%20S.png)
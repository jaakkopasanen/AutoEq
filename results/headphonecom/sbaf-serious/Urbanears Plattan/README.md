# Urbanears Plattan

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.9; 45 5.8; 49 5.6; 54 5.5; 60 5.3; 66 5.2; 72 5.0; 79 4.8; 87 4.7; 96 4.7; 106 4.6; 116 4.6; 128 4.8; 141 4.5; 155 4.1; 170 3.8; 187 3.6; 206 3.6; 227 3.8; 249 3.8; 274 4.0; 302 4.4; 332 5.0; 365 5.5; 402 5.4; 442 4.4; 486 3.5; 535 2.8; 588 2.3; 647 1.7; 712 1.0; 783 0.4; 861 -0.1; 947 -0.3; 1042 0.5; 1146 2.3; 1261 3.2; 1387 4.0; 1526 5.6; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Urbanears Plattan GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Urbanears Plattan ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.29 | 6.0 dB  |
| Peaking | 152 Hz  | 0.77 | 2.3 dB  |
| Peaking | 376 Hz  | 1.95 | 4.6 dB  |
| Peaking | 2085 Hz | 1.16 | 5.9 dB  |
| Peaking | 4759 Hz | 1.37 | 5.7 dB  |
| Peaking | 927 Hz  | 3.9  | -2.2 dB |
| Peaking | 1526 Hz | 5.19 | 1.6 dB  |
| Peaking | 4808 Hz | 5.94 | -1.0 dB |
| Peaking | 6419 Hz | 2.98 | 3.7 dB  |
| Peaking | 7550 Hz | 1.96 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Urbanears%20Plattan/Urbanears%20Plattan.png)
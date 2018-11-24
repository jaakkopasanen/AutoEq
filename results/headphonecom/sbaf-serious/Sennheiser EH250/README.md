# Sennheiser EH250

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.9; 60 4.9; 66 4.3; 72 3.8; 79 2.9; 87 2.3; 96 1.8; 106 1.4; 116 1.3; 128 1.6; 141 3.2; 155 3.6; 170 3.7; 187 3.9; 206 4.4; 227 4.9; 249 5.1; 274 4.8; 302 2.3; 332 1.3; 365 2.1; 402 2.4; 442 2.2; 486 1.4; 535 0.7; 588 0.5; 647 0.4; 712 0.5; 783 0.7; 861 0.4; 947 0.1; 1042 0.0; 1146 0.3; 1261 0.2; 1387 -0.0; 1526 -0.2; 1678 -0.3; 1846 0.1; 2031 0.5; 2234 1.3; 2457 1.6; 2703 2.4; 2973 4.1; 3270 6.0; 3597 6.0; 3957 -1.1; 4353 -1.3; 4788 2.5; 5267 3.1; 5793 5.9; 6373 3.6; 7010 -0.9; 7711 -0.7; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.1; 13660 -3.9; 15026 -3.9; 16529 -2.8; 18182 -1.8; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser EH250 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser EH250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.63 | 6.7 dB  |
| Peaking | 231 Hz   | 1.43 | 4.7 dB  |
| Peaking | 4454 Hz  | 0.69 | 3.3 dB  |
| Peaking | 12072 Hz | 2.42 | 5.1 dB  |
| Peaking | 13430 Hz | 1.01 | -6.4 dB |
| Peaking | 1738 Hz  | 1.88 | -1.3 dB |
| Peaking | 3476 Hz  | 3.5  | 6.0 dB  |
| Peaking | 4097 Hz  | 4.89 | -8.2 dB |
| Peaking | 5972 Hz  | 4.44 | 4.8 dB  |
| Peaking | 7080 Hz  | 5.45 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20EH250/Sennheiser%20EH250.png)
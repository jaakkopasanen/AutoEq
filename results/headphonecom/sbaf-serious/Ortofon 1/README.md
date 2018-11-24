# Ortofon 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 6.0; 274 6.0; 302 6.0; 332 5.7; 365 2.5; 402 -0.2; 442 -1.6; 486 -2.1; 535 -1.9; 588 -1.2; 647 1.2; 712 0.9; 783 0.6; 861 0.3; 947 0.3; 1042 -0.2; 1146 0.5; 1261 0.9; 1387 0.5; 1526 -0.7; 1678 -0.4; 1846 2.5; 2031 5.8; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 2.0; 4353 1.8; 4788 0.4; 5267 -1.2; 5793 5.3; 6373 5.5; 7010 2.5; 7711 0.2; 8482 -1.8; 9330 -2.1; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.3; 16529 -1.2; 18182 -1.7; 20000 -7.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ortofon 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ortofon 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 100 Hz   | 0.11 | 6.6 dB  |
| Peaking | 483 Hz   | 2.68 | -6.6 dB |
| Peaking | 2491 Hz  | 0.32 | -6.8 dB |
| Peaking | 2755 Hz  | 1    | 13.2 dB |
| Peaking | 6284 Hz  | 4.84 | 7.8 dB  |
| Peaking | 304 Hz   | 5.25 | 2.1 dB  |
| Peaking | 1310 Hz  | 4.2  | 2.7 dB  |
| Peaking | 1652 Hz  | 1.75 | -3.4 dB |
| Peaking | 2010 Hz  | 4.86 | 4.6 dB  |
| Peaking | 11642 Hz | 3.93 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ortofon%201/Ortofon%201.png)
# Sony MDR-SA3000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.4; 79 4.5; 87 3.8; 96 3.4; 106 2.6; 116 2.1; 128 1.7; 141 1.3; 155 1.0; 170 1.3; 187 1.2; 206 1.2; 227 1.4; 249 1.3; 274 1.3; 302 1.2; 332 0.9; 365 0.4; 402 0.4; 442 0.2; 486 -0.4; 535 -0.9; 588 -0.7; 647 -1.3; 712 -1.8; 783 -1.6; 861 -1.3; 947 -0.5; 1042 0.7; 1146 1.9; 1261 3.3; 1387 4.1; 1526 4.1; 1678 4.3; 1846 3.5; 2031 2.3; 2234 -0.5; 2457 -1.5; 2703 -1.8; 2973 -0.8; 3270 0.7; 3597 4.2; 3957 6.0; 4353 5.3; 4788 2.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 1.6; 7711 -0.6; 8482 -3.6; 9330 -4.0; 10263 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-SA3000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-SA3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.46 | 6.6 dB  |
| Peaking | 1530 Hz | 3.17 | 5.0 dB  |
| Peaking | 3974 Hz | 5.96 | 5.7 dB  |
| Peaking | 5814 Hz | 2.84 | 6.8 dB  |
| Peaking | 8801 Hz | 4.1  | -5.5 dB |
| Peaking | 67 Hz   | 5.3  | 0.9 dB  |
| Peaking | 739 Hz  | 1.5  | -3.4 dB |
| Peaking | 1304 Hz | 0.35 | 1.6 dB  |
| Peaking | 1992 Hz | 5.83 | 2.3 dB  |
| Peaking | 2486 Hz | 2.08 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-SA3000/Sony%20MDR-SA3000.png)
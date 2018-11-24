# Sennheiser PX 200-IIi

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.8; 79 5.1; 87 4.4; 96 4.4; 106 4.4; 116 3.5; 128 2.8; 141 2.0; 155 1.4; 170 1.2; 187 1.0; 206 0.7; 227 0.4; 249 0.2; 274 0.3; 302 0.1; 332 0.1; 365 0.1; 402 0.8; 442 0.9; 486 0.5; 535 0.5; 588 1.0; 647 1.7; 712 2.1; 783 2.2; 861 2.0; 947 1.0; 1042 0.5; 1146 1.6; 1261 2.3; 1387 1.4; 1526 0.1; 1678 -0.8; 1846 -1.3; 2031 -1.1; 2234 -1.1; 2457 0.2; 2703 1.4; 2973 2.6; 3270 3.6; 3597 4.5; 3957 5.8; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 200-IIi GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 200-IIi ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.43 | 6.7 dB  |
| Peaking | 751 Hz  | 2.96 | 2.2 dB  |
| Peaking | 1271 Hz | 4.32 | 2.2 dB  |
| Peaking | 1988 Hz | 2.19 | -2.6 dB |
| Peaking | 4621 Hz | 1.32 | 6.9 dB  |
| Peaking | 28 Hz   | 0.57 | 1.7 dB  |
| Peaking | 36 Hz   | 1.43 | -2.3 dB |
| Peaking | 4773 Hz | 6.19 | -1.1 dB |
| Peaking | 6367 Hz | 2.84 | 3.9 dB  |
| Peaking | 7592 Hz | 1.95 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PX%20200-IIi/Sennheiser%20PX%20200-IIi.png)
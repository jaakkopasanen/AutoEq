# Sennheiser MM 550-X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 5.9; 128 5.9; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 6.0; 274 6.0; 302 6.0; 332 6.0; 365 6.0; 402 6.0; 442 5.7; 486 5.1; 535 4.2; 588 3.3; 647 2.4; 712 1.3; 783 0.2; 861 -0.2; 947 -0.1; 1042 0.3; 1146 0.8; 1261 1.1; 1387 0.6; 1526 -0.2; 1678 -1.2; 1846 -3.5; 2031 -6.6; 2234 -6.7; 2457 -3.5; 2703 -1.1; 2973 1.7; 3270 5.1; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.5; 9330 -1.5; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MM 550-X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MM 550-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 50 Hz    | 0.16 | 6.2 dB   |
| Peaking | 368 Hz   | 1.2  | 3.6 dB   |
| Peaking | 2186 Hz  | 2.54 | -10.6 dB |
| Peaking | 4465 Hz  | 0.77 | 7.7 dB   |
| Peaking | 8671 Hz  | 2.58 | -4.8 dB  |
| Peaking | 527 Hz   | 3.07 | 0.9 dB   |
| Peaking | 857 Hz   | 2.5  | -2.0 dB  |
| Peaking | 1297 Hz  | 2.86 | 1.0 dB   |
| Peaking | 6296 Hz  | 7.79 | 1.6 dB   |
| Peaking | 12730 Hz | 0.33 | -0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20MM%20550-X/Sennheiser%20MM%20550-X.png)
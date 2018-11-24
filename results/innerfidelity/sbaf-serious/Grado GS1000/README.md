# Grado GS1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.7; 34 5.0; 37 4.2; 41 3.1; 45 1.8; 49 0.5; 54 -0.8; 60 -2.3; 66 -3.6; 72 -4.6; 79 -5.7; 87 -6.6; 96 -7.3; 106 -7.4; 116 -7.2; 128 -6.8; 141 -6.3; 155 -5.7; 170 -5.0; 187 -4.4; 206 -3.8; 227 -3.1; 249 -2.6; 274 -2.0; 302 -1.9; 332 -2.0; 365 -1.6; 402 -1.3; 442 -0.8; 486 -0.7; 535 -0.7; 588 -0.3; 647 -0.2; 712 -0.3; 783 0.1; 861 -0.1; 947 -0.0; 1042 -0.0; 1146 -0.4; 1261 -0.7; 1387 -1.3; 1526 -1.7; 1678 -0.7; 1846 -1.9; 2031 -1.6; 2234 -1.3; 2457 -1.2; 2703 -1.4; 2973 -1.2; 3270 -0.8; 3597 -2.9; 3957 -5.3; 4353 -9.9; 4788 -6.7; 5267 -8.4; 5793 -10.5; 6373 -11.3; 7010 -9.0; 7711 -5.9; 8482 -6.7; 9330 -10.4; 10263 -9.7; 11289 -4.8; 12418 -2.2; 13660 -1.7; 15026 -0.0; 16529 0.0; 18182 0.0; 20000 -1.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GS1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.63 | 7.9 dB   |
| Peaking | 98 Hz    | 0.66 | -9.0 dB  |
| Peaking | 261 Hz   | 2.44 | 0.2 dB   |
| Peaking | 5837 Hz  | 1.37 | -10.5 dB |
| Peaking | 9873 Hz  | 3.78 | -8.8 dB  |
| Peaking | 889 Hz   | 0.99 | 1.7 dB   |
| Peaking | 2172 Hz  | 0.37 | -2.2 dB  |
| Peaking | 3846 Hz  | 1.17 | 4.5 dB   |
| Peaking | 4251 Hz  | 7.03 | -7.1 dB  |
| Peaking | 22267 Hz | 3.61 | 0.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20GS1000/Grado%20GS1000.png)
# Yamaha HP1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.0; 25 4.6; 28 4.0; 31 3.6; 34 3.3; 37 3.0; 41 2.7; 45 2.5; 49 2.3; 54 2.0; 60 1.8; 66 1.6; 72 1.3; 79 1.1; 87 0.9; 96 0.5; 106 0.1; 116 -0.0; 128 -0.4; 141 -0.7; 155 -0.8; 170 -0.9; 187 -1.1; 206 -1.2; 227 -1.1; 249 -1.2; 274 -1.0; 302 -0.9; 332 -1.0; 365 -0.9; 402 -1.0; 442 -0.8; 486 -1.0; 535 -1.1; 588 -0.8; 647 -0.8; 712 -1.0; 783 -0.6; 861 -0.5; 947 -0.2; 1042 0.3; 1146 1.2; 1261 2.4; 1387 2.9; 1526 2.8; 1678 3.3; 1846 3.2; 2031 2.1; 2234 0.6; 2457 1.4; 2703 1.3; 2973 3.0; 3270 4.6; 3597 5.2; 3957 4.6; 4353 3.6; 4788 4.7; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha HP1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HP1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.2  | 5.1 dB  |
| Peaking | 48 Hz   | 1.85 | 1.6 dB  |
| Peaking | 1605 Hz | 2.63 | 3.4 dB  |
| Peaking | 3574 Hz | 3.06 | 4.7 dB  |
| Peaking | 5651 Hz | 2.77 | 6.2 dB  |
| Peaking | 79 Hz   | 1.5  | 1.2 dB  |
| Peaking | 298 Hz  | 0.25 | -1.2 dB |
| Peaking | 1252 Hz | 5.07 | 1.6 dB  |
| Peaking | 1886 Hz | 9.19 | 1.1 dB  |
| Peaking | 8181 Hz | 4.97 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20HP1/Yamaha%20HP1.png)
# Yamaha YH100 Sn130216

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.8; 37 5.6; 41 5.4; 45 5.3; 49 5.2; 54 5.1; 60 5.0; 66 4.9; 72 4.7; 79 4.5; 87 4.2; 96 3.8; 106 3.6; 116 3.4; 128 3.1; 141 2.8; 155 2.6; 170 2.5; 187 2.4; 206 2.2; 227 2.2; 249 2.2; 274 2.2; 302 2.3; 332 2.1; 365 2.0; 402 1.9; 442 1.9; 486 1.5; 535 1.3; 588 1.2; 647 0.8; 712 0.2; 783 -0.1; 861 -0.6; 947 -0.1; 1042 0.6; 1146 2.2; 1261 5.1; 1387 6.0; 1526 6.0; 1678 6.0; 1846 5.9; 2031 3.5; 2234 1.2; 2457 4.1; 2703 5.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha YH100 Sn130216 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha YH100 Sn130216 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.7  | 3.9 dB  |
| Peaking | 60 Hz   | 0.39 | 4.1 dB  |
| Peaking | 338 Hz  | 1.57 | 1.4 dB  |
| Peaking | 1526 Hz | 2.64 | 5.8 dB  |
| Peaking | 4145 Hz | 1.03 | 6.7 dB  |
| Peaking | 921 Hz  | 3.15 | -1.9 dB |
| Peaking | 1271 Hz | 7.26 | 1.9 dB  |
| Peaking | 4258 Hz | 5.71 | -1.2 dB |
| Peaking | 6347 Hz | 2.54 | 4.6 dB  |
| Peaking | 7526 Hz | 1.78 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20YH100%20Sn130216/Yamaha%20YH100%20Sn130216.png)
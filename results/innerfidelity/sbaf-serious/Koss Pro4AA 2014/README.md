# Koss Pro4AA 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 5.0; 206 4.0; 227 2.9; 249 1.6; 274 0.3; 302 -1.0; 332 -1.9; 365 -3.1; 402 -4.0; 442 -4.5; 486 -4.6; 535 -4.9; 588 -3.8; 647 -3.2; 712 -2.4; 783 -1.4; 861 -0.8; 947 -0.1; 1042 0.2; 1146 0.2; 1261 -0.4; 1387 -1.9; 1526 -3.9; 1678 -5.9; 1846 -7.7; 2031 -9.7; 2234 -11.4; 2457 -10.4; 2703 -7.5; 2973 -3.1; 3270 0.8; 3597 3.0; 3957 2.1; 4353 -0.1; 4788 0.1; 5267 3.5; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.9; 10263 -0.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Pro4AA 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Pro4AA 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 172 Hz  | 0.08 | 7.2 dB   |
| Peaking | 465 Hz  | 0.89 | -11.7 dB |
| Peaking | 2266 Hz | 1.38 | -15.1 dB |
| Peaking | 3484 Hz | 3.37 | 7.1 dB   |
| Peaking | 5984 Hz | 3.83 | 7.3 dB   |
| Peaking | 18 Hz   | 1.2  | 1.5 dB   |
| Peaking | 85 Hz   | 0.2  | -0.7 dB  |
| Peaking | 164 Hz  | 2.26 | 1.9 dB   |
| Peaking | 1162 Hz | 4.82 | 1.3 dB   |
| Peaking | 9432 Hz | 6.16 | -1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Pro4AA%202014/Koss%20Pro4AA%202014.png)
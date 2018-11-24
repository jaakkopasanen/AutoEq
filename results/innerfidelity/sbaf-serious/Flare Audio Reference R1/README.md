# Flare Audio Reference R1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.0; 60 3.2; 66 1.6; 72 0.3; 79 -1.0; 87 -2.1; 96 -2.9; 106 -3.9; 116 -4.4; 128 -4.8; 141 -5.1; 155 -5.3; 170 -5.3; 187 -5.4; 206 -5.5; 227 -5.5; 249 -5.6; 274 -5.7; 302 -5.7; 332 -5.6; 365 -5.6; 402 -5.7; 442 -5.9; 486 -6.6; 535 -7.2; 588 -7.3; 647 -7.4; 712 -7.1; 783 -6.0; 861 -4.2; 947 -1.7; 1042 1.5; 1146 5.0; 1261 6.0; 1387 6.0; 1526 6.0; 1678 1.3; 1846 -3.9; 2031 -4.2; 2234 -0.2; 2457 3.5; 2703 5.7; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Flare Audio Reference R1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Flare Audio Reference R1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 45 Hz   | 0.45 | 10.1 dB  |
| Peaking | 103 Hz  | 0.59 | -8.7 dB  |
| Peaking | 1269 Hz | 1.87 | 17.7 dB  |
| Peaking | 1379 Hz | 0.31 | -13.6 dB |
| Peaking | 3617 Hz | 0.77 | 14.6 dB  |
| Peaking | 1562 Hz | 7.58 | 5.4 dB   |
| Peaking | 1933 Hz | 4.46 | -5.7 dB  |
| Peaking | 2621 Hz | 3.71 | 4.3 dB   |
| Peaking | 5929 Hz | 2.1  | 7.4 dB   |
| Peaking | 5962 Hz | 0.84 | -4.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Flare%20Audio%20Reference%20R1/Flare%20Audio%20Reference%20R1.png)
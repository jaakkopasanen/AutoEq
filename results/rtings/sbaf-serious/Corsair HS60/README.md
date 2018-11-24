# Corsair HS60

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 21 -2.1; 23 -2.4; 25 -2.7; 28 -3.2; 31 -3.6; 34 -3.9; 37 -4.1; 41 -4.4; 45 -4.6; 49 -4.8; 54 -5.0; 60 -5.2; 66 -5.4; 72 -5.6; 79 -5.8; 87 -6.1; 96 -6.3; 106 -6.6; 116 -6.6; 128 -6.6; 141 -6.4; 155 -6.1; 170 -5.5; 187 -4.7; 206 -3.8; 227 -2.7; 249 -1.8; 274 -0.6; 302 0.4; 332 1.0; 365 1.6; 402 1.8; 442 1.5; 486 0.9; 535 -0.0; 588 -1.1; 647 -1.6; 712 -1.6; 783 -1.4; 861 -0.7; 947 0.7; 1042 -0.1; 1146 0.4; 1261 0.7; 1387 0.5; 1526 0.3; 1678 0.1; 1846 0.1; 2031 -0.1; 2234 -0.0; 2457 -0.1; 2703 -0.3; 2973 0.2; 3270 1.9; 3597 4.8; 3957 4.4; 4353 -0.9; 4788 -3.0; 5267 0.4; 5793 2.3; 6373 5.2; 7010 2.5; 7711 -0.6; 8482 -8.1; 9330 -8.8; 10263 -3.8; 11289 -0.3; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Corsair HS60 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Corsair HS60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 56 Hz   | 0.62 | -4.9 dB  |
| Peaking | 136 Hz  | 1.46 | -5.1 dB  |
| Peaking | 6372 Hz | 5.91 | 4.6 dB   |
| Peaking | 7143 Hz | 2.33 | 2.9 dB   |
| Peaking | 8864 Hz | 3.9  | -11.8 dB |
| Peaking | 213 Hz  | 1.72 | -2.2 dB  |
| Peaking | 456 Hz  | 0.75 | 4.0 dB   |
| Peaking | 638 Hz  | 1.71 | -4.5 dB  |
| Peaking | 3753 Hz | 5.54 | 6.2 dB   |
| Peaking | 4649 Hz | 6.45 | -4.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Corsair%20HS60/Corsair%20HS60.png)
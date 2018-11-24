# Koss KSC75

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.5; 54 4.4; 60 3.1; 66 2.0; 72 1.1; 79 0.4; 87 -0.4; 96 -1.1; 106 -1.7; 116 -2.2; 128 -2.5; 141 -2.7; 155 -2.7; 170 -2.3; 187 -2.1; 206 -2.1; 227 -1.9; 249 -1.7; 274 -1.4; 302 -1.1; 332 -0.9; 365 -0.7; 402 -0.6; 442 -0.4; 486 -0.2; 535 -0.0; 588 0.1; 647 0.3; 712 0.4; 783 0.3; 861 0.1; 947 -0.0; 1042 0.1; 1146 0.2; 1261 -0.0; 1387 -0.9; 1526 -2.1; 1678 -2.9; 1846 -3.8; 2031 -4.7; 2234 -4.9; 2457 -4.5; 2703 -3.2; 2973 -2.2; 3270 -0.1; 3597 5.7; 3957 5.0; 4353 -0.9; 4788 -6.3; 5267 -0.8; 5793 4.0; 6373 4.2; 7010 2.3; 7711 0.2; 8482 -3.0; 9330 -4.5; 10263 -0.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss KSC75 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KSC75 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 1.25 | 7.4 dB   |
| Peaking | 2344 Hz  | 1.84 | -4.8 dB  |
| Peaking | 3896 Hz  | 2.19 | 18.1 dB  |
| Peaking | 4757 Hz  | 1.44 | -20.4 dB |
| Peaking | 5916 Hz  | 2.59 | 13.9 dB  |
| Peaking | 53 Hz    | 2.32 | 2.8 dB   |
| Peaking | 145 Hz   | 0.76 | -3.0 dB  |
| Peaking | 856 Hz   | 1.23 | 1.0 dB   |
| Peaking | 9115 Hz  | 4.25 | -6.3 dB  |
| Peaking | 10022 Hz | 1.41 | 2.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Koss%20KSC75/Koss%20KSC75.png)
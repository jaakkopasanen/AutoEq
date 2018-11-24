# Sony MDR-ZX110NC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.8; 25 2.1; 28 1.2; 31 0.4; 34 -0.3; 37 -0.8; 41 -1.5; 45 -2.1; 49 -2.5; 54 -3.1; 60 -3.6; 66 -4.2; 72 -4.6; 79 -4.9; 87 -5.3; 96 -5.5; 106 -5.6; 116 -5.7; 128 -5.6; 141 -5.4; 155 -5.3; 170 -5.0; 187 -4.8; 206 -4.4; 227 -4.1; 249 -3.8; 274 -3.6; 302 -3.3; 332 -2.7; 365 -1.7; 402 -0.3; 442 0.2; 486 -0.1; 535 -0.2; 588 -0.2; 647 -0.2; 712 -0.2; 783 -0.1; 861 0.3; 947 0.3; 1042 -0.5; 1146 -1.8; 1261 -2.3; 1387 -2.7; 1526 -2.4; 1678 -1.7; 1846 -0.5; 2031 0.6; 2234 2.0; 2457 3.3; 2703 3.8; 2973 3.6; 3270 3.6; 3597 4.9; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 3.6; 7010 -0.4; 7711 -2.5; 8482 -5.7; 9330 -8.3; 10263 -4.6; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX110NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX110NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 1.41 | 4.3 dB   |
| Peaking | 105 Hz   | 0.59 | -5.6 dB  |
| Peaking | 237 Hz   | 1.58 | -1.7 dB  |
| Peaking | 4755 Hz  | 1.18 | 7.3 dB   |
| Peaking | 9095 Hz  | 3.01 | -10.2 dB |
| Peaking | 1014 Hz  | 0.66 | 1.6 dB   |
| Peaking | 1412 Hz  | 1.56 | -4.6 dB  |
| Peaking | 2523 Hz  | 3.49 | 2.2 dB   |
| Peaking | 7246 Hz  | 8.29 | -1.8 dB  |
| Peaking | 11286 Hz | 6.99 | 2.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sony%20MDR-ZX110NC/Sony%20MDR-ZX110NC.png)
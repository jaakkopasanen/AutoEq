# Sony MDR-7506

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 -3.0; 23 -3.6; 25 -4.1; 28 -4.9; 31 -5.5; 34 -5.9; 37 -6.2; 41 -6.4; 45 -6.5; 49 -6.5; 54 -6.3; 60 -6.1; 66 -5.8; 72 -5.4; 79 -5.0; 87 -4.7; 96 -4.6; 106 -4.5; 116 -4.2; 128 -3.7; 141 -3.1; 155 -2.6; 170 -1.9; 187 -1.0; 206 -0.1; 227 1.2; 249 2.7; 274 2.2; 302 -0.0; 332 -0.6; 365 -0.7; 402 -0.9; 442 -0.9; 486 -0.7; 535 -0.6; 588 -0.5; 647 -0.2; 712 -0.1; 783 -0.2; 861 -0.1; 947 0.0; 1042 -0.1; 1146 -0.3; 1261 -0.6; 1387 -1.3; 1526 -2.4; 1678 -3.1; 1846 -3.5; 2031 -3.9; 2234 -3.4; 2457 -3.1; 2703 -3.6; 2973 -4.0; 3270 -2.9; 3597 -1.4; 3957 -2.8; 4353 -6.3; 4788 -3.7; 5267 1.7; 5793 5.5; 6373 4.7; 7010 2.3; 7711 -0.5; 8482 -4.0; 9330 -7.2; 10263 -6.7; 11289 -0.6; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7506 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7506 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 50 Hz    | 0.57 | -6.8 dB |
| Peaking | 2309 Hz  | 1.25 | -4.0 dB |
| Peaking | 4478 Hz  | 4.81 | -7.5 dB |
| Peaking | 5940 Hz  | 2.74 | 7.6 dB  |
| Peaking | 9491 Hz  | 3.57 | -8.9 dB |
| Peaking | 124 Hz   | 2.43 | -1.2 dB |
| Peaking | 253 Hz   | 4.71 | 4.1 dB  |
| Peaking | 5012 Hz  | 5.32 | -0.4 dB |
| Peaking | 11814 Hz | 7.39 | 1.7 dB  |
| Peaking | 21490 Hz | 1.63 | 0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20MDR-7506/Sony%20MDR-7506.png)
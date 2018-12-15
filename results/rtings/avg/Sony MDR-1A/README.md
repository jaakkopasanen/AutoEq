# Sony MDR-1A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 21 -2.1; 23 -2.4; 25 -2.7; 28 -3.0; 31 -3.2; 34 -3.2; 37 -3.1; 41 -3.1; 45 -3.0; 49 -3.0; 54 -2.9; 60 -2.8; 66 -3.0; 72 -3.1; 79 -3.4; 87 -3.7; 96 -4.0; 106 -4.2; 116 -4.2; 128 -4.0; 141 -3.6; 155 -3.0; 170 -2.3; 187 -1.5; 206 -0.9; 227 -0.6; 249 -0.9; 274 0.1; 302 1.1; 332 1.6; 365 1.9; 402 1.9; 442 1.8; 486 1.4; 535 1.0; 588 0.6; 647 0.4; 712 0.3; 783 0.2; 861 0.0; 947 -0.0; 1042 -0.0; 1146 -0.1; 1261 -0.3; 1387 -0.6; 1526 -0.9; 1678 -1.2; 1846 -1.6; 2031 -1.7; 2234 -1.0; 2457 0.5; 2703 1.2; 2973 1.4; 3270 1.4; 3597 2.1; 3957 -1.0; 4353 -0.8; 4788 2.5; 5267 1.8; 5793 2.3; 6373 2.4; 7010 1.8; 7711 -1.5; 8482 -6.7; 9330 -7.8; 10263 -3.5; 11289 -0.1; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.1; 18182 -3.2; 20000 -3.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.65 | -2.9 dB  |
| Peaking | 116 Hz   | 1.06 | -3.8 dB  |
| Peaking | 380 Hz   | 1.79 | 2.6 dB   |
| Peaking | 6575 Hz  | 1.67 | 3.9 dB   |
| Peaking | 8933 Hz  | 3.5  | -10.4 dB |
| Peaking | 2537 Hz  | 1.27 | -4.2 dB  |
| Peaking | 2730 Hz  | 2.57 | 5.3 dB   |
| Peaking | 3503 Hz  | 9.66 | 2.3 dB   |
| Peaking | 16347 Hz | 0.74 | 1.8 dB   |
| Peaking | 19131 Hz | 1.2  | -5.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-1A/Sony%20MDR-1A.png)
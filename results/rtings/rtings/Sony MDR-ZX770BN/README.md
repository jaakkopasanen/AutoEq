# Sony MDR-ZX770BN

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 21 -4.4; 23 -5.1; 25 -5.7; 28 -6.5; 31 -7.1; 34 -7.4; 37 -7.6; 41 -7.7; 45 -7.8; 49 -7.8; 54 -7.7; 60 -7.5; 66 -7.4; 72 -7.2; 79 -7.0; 87 -6.7; 96 -6.5; 106 -6.6; 116 -6.6; 128 -6.7; 141 -6.4; 155 -5.9; 170 -6.2; 187 -7.0; 206 -6.8; 227 -6.4; 249 -6.2; 274 -5.9; 302 -5.4; 332 -4.7; 365 -3.7; 402 -2.6; 442 -1.6; 486 -0.7; 535 0.1; 588 0.1; 647 0.1; 712 -0.2; 783 -0.3; 861 -0.1; 947 -0.1; 1042 -0.2; 1146 -0.7; 1261 -0.7; 1387 -0.5; 1526 -1.1; 1678 -3.0; 1846 -5.8; 2031 -7.8; 2234 -6.9; 2457 -5.1; 2703 -3.8; 2973 -3.7; 3270 -1.8; 3597 2.5; 3957 -4.2; 4353 -7.9; 4788 -8.6; 5267 -5.5; 5793 -0.7; 6373 -0.2; 7010 -1.6; 7711 -4.7; 8482 -8.9; 9330 -11.5; 10263 -10.9; 11289 -7.3; 12418 -2.9; 13660 -1.7; 15026 -5.0; 16529 -8.8; 18182 -7.7; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX770BN GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX770BN ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--1.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 67 Hz    | 0.23 | -7.6 dB  |
| Peaking | 2161 Hz  | 2.37 | -7.4 dB  |
| Peaking | 9590 Hz  | 2.14 | -11.7 dB |
| Peaking | 17279 Hz | 2.04 | -9.6 dB  |
| Peaking | 24000 Hz | 2.2  | -7.0 dB  |
| Peaking | 274 Hz   | 0.9  | -6.9 dB  |
| Peaking | 323 Hz   | 0.47 | 5.2 dB   |
| Peaking | 3610 Hz  | 7.66 | 7.8 dB   |
| Peaking | 4655 Hz  | 2.28 | -9.7 dB  |
| Peaking | 6136 Hz  | 2.83 | 6.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sony%20MDR-ZX770BN/Sony%20MDR-ZX770BN.png)
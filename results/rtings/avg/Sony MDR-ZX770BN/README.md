# Sony MDR-ZX770BN
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.6dB
GraphicEQ: 21 -4.4; 23 -5.1; 25 -5.7; 28 -6.5; 31 -7.1; 34 -7.4; 37 -7.6; 41 -7.7; 45 -7.8; 49 -7.8; 54 -7.7; 60 -7.5; 66 -7.4; 72 -7.2; 79 -7.0; 87 -6.7; 96 -6.5; 106 -6.6; 116 -6.6; 128 -6.7; 141 -6.4; 155 -5.9; 170 -6.2; 187 -7.0; 206 -6.8; 227 -6.4; 249 -6.2; 274 -5.9; 302 -5.4; 332 -4.7; 365 -3.7; 402 -2.6; 442 -1.6; 486 -0.7; 535 0.1; 588 0.1; 647 0.1; 712 -0.2; 783 -0.3; 861 -0.1; 947 -0.1; 1042 -0.2; 1146 -0.7; 1261 -0.7; 1387 -0.5; 1526 -1.1; 1678 -3.0; 1846 -5.8; 2031 -7.8; 2234 -6.9; 2457 -5.1; 2703 -4.0; 2973 -4.2; 3270 -2.6; 3597 1.5; 3957 -5.4; 4353 -9.2; 4788 -10.3; 5267 -8.1; 5793 -3.2; 6373 -1.4; 7010 -2.4; 7711 -6.1; 8482 -9.6; 9330 -10.1; 10263 -9.2; 11289 -8.1; 12418 -6.2; 13660 -5.0; 15026 -7.6; 16529 -11.8; 18182 -12.0; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX770BN GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-16**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX770BN ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--1.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 67 Hz    | 0.23 | -7.6 dB  |
| Peaking | 2081 Hz  | 3.84 | -6.8 dB  |
| Peaking | 8972 Hz  | 0.45 | -7.0 dB  |
| Peaking | 17655 Hz | 1.79 | -10.2 dB |
| Peaking | 22208 Hz | 1    | -10.9 dB |
| Peaking | 619 Hz   | 2.12 | 2.1 dB   |
| Peaking | 3609 Hz  | 7.43 | 8.5 dB   |
| Peaking | 4783 Hz  | 1.48 | -15.5 dB |
| Peaking | 6379 Hz  | 1.05 | 16.2 dB  |
| Peaking | 8785 Hz  | 1.76 | -9.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-ZX770BN/Sony%20MDR-ZX770BN.png)
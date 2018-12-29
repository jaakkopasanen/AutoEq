# Sony MDR-XB1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.1; 23 -1.9; 25 -2.7; 28 -3.9; 31 -4.9; 34 -5.7; 37 -6.0; 41 -6.4; 45 -6.6; 49 -6.9; 54 -7.6; 60 -8.2; 66 -8.6; 72 -8.8; 79 -9.1; 87 -9.6; 96 -9.9; 106 -10.2; 116 -10.5; 128 -10.8; 141 -11.0; 155 -11.1; 170 -11.3; 187 -11.4; 206 -11.3; 227 -11.1; 249 -10.8; 274 -10.1; 302 -9.3; 332 -8.5; 365 -7.8; 402 -7.0; 442 -6.0; 486 -4.8; 535 -3.8; 588 -1.6; 647 0.7; 712 2.3; 783 4.1; 861 4.0; 947 1.8; 1042 -1.4; 1146 -4.4; 1261 -4.3; 1387 -2.0; 1526 0.8; 1678 3.9; 1846 6.0; 2031 6.0; 2234 -0.5; 2457 -8.3; 2703 -7.0; 2973 -4.5; 3270 -3.3; 3597 -2.7; 3957 -2.9; 4353 -2.8; 4788 1.5; 5267 5.9; 5793 1.2; 6373 -3.4; 7010 -0.7; 7711 0.3; 8482 0.0; 9330 -0.4; 10263 -1.6; 11289 -0.9; 12418 -0.0; 13660 0.0; 15026 -1.4; 16529 -2.4; 18182 -1.6; 20000 -0.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 103 Hz   | 0.37 | -9.3 dB  |
| Peaking | 289 Hz   | 0.85 | -6.9 dB  |
| Peaking | 1277 Hz  | 3.04 | -10.7 dB |
| Peaking | 1978 Hz  | 0.73 | 25.8 dB  |
| Peaking | 2521 Hz  | 1.18 | -27.9 dB |
| Peaking | 497 Hz   | 3.45 | -1.8 dB  |
| Peaking | 794 Hz   | 4.62 | 4.0 dB   |
| Peaking | 5235 Hz  | 5.66 | 12.3 dB  |
| Peaking | 5413 Hz  | 1.77 | -5.3 dB  |
| Peaking | 16881 Hz | 1.56 | -2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-XB1000/Sony%20MDR-XB1000.png)
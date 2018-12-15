# Sony MDR-Z7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.9; 45 5.7; 49 5.5; 54 5.2; 60 4.8; 66 4.3; 72 3.9; 79 3.4; 87 2.7; 96 1.9; 106 1.2; 116 0.5; 128 0.0; 141 -0.6; 155 -1.2; 170 -1.6; 187 -1.5; 206 -1.0; 227 -0.3; 249 0.4; 274 0.9; 302 1.2; 332 1.5; 365 1.7; 402 1.9; 442 1.8; 486 1.5; 535 1.3; 588 1.0; 647 0.4; 712 -0.4; 783 -1.0; 861 -1.2; 947 -0.6; 1042 0.5; 1146 1.9; 1261 3.3; 1387 3.7; 1526 2.9; 1678 1.6; 1846 0.5; 2031 -0.3; 2234 -1.1; 2457 -2.1; 2703 -2.0; 2973 -0.1; 3270 2.9; 3597 5.8; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 3.9; 6373 0.4; 7010 -3.2; 7711 -6.4; 8482 -7.6; 9330 -6.3; 10263 -3.0; 11289 -0.1; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.3; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-Z7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.69 | 6.8 dB   |
| Peaking | 1373 Hz  | 4.16 | 3.5 dB   |
| Peaking | 2621 Hz  | 2.12 | -6.8 dB  |
| Peaking | 4443 Hz  | 0.85 | 9.2 dB   |
| Peaking | 8157 Hz  | 2.02 | -11.6 dB |
| Peaking | 74 Hz    | 2.09 | 1.2 dB   |
| Peaking | 178 Hz   | 1.3  | -3.5 dB  |
| Peaking | 354 Hz   | 0.59 | 2.3 dB   |
| Peaking | 814 Hz   | 2.57 | -2.7 dB  |
| Peaking | 11482 Hz | 6.85 | 1.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sony%20MDR-Z7/Sony%20MDR-Z7.png)
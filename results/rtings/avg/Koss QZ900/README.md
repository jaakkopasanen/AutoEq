# Koss QZ900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 -12.1; 23 -11.9; 25 -11.7; 28 -11.6; 31 -11.4; 34 -11.3; 37 -11.1; 41 -11.0; 45 -10.8; 49 -10.7; 54 -10.6; 60 -10.5; 66 -10.4; 72 -10.2; 79 -10.0; 87 -10.0; 96 -10.2; 106 -10.6; 116 -10.9; 128 -10.9; 141 -10.9; 155 -10.7; 170 -10.3; 187 -9.8; 206 -9.3; 227 -8.7; 249 -7.8; 274 -6.1; 302 -5.3; 332 -5.0; 365 -4.2; 402 -3.4; 442 -2.7; 486 -2.4; 535 -2.3; 588 -2.2; 647 -2.1; 712 -1.7; 783 -1.2; 861 -0.6; 947 -0.1; 1042 0.1; 1146 0.0; 1261 -0.4; 1387 -1.2; 1526 -1.8; 1678 -4.1; 1846 -5.8; 2031 -5.8; 2234 -2.2; 2457 2.2; 2703 -7.7; 2973 -8.7; 3270 -2.1; 3597 1.7; 3957 3.2; 4353 2.3; 4788 5.2; 5267 0.5; 5793 3.5; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.6; 18182 -3.6; 20000 -2.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss QZ900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss QZ900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 1.35 | -11.8 dB |
| Peaking | 34 Hz    | 0.42 | -8.9 dB  |
| Peaking | 151 Hz   | 0.63 | -8.0 dB  |
| Peaking | 227 Hz   | 1.71 | -1.2 dB  |
| Peaking | 1920 Hz  | 3.07 | -6.0 dB  |
| Peaking | 2433 Hz  | 9.01 | 7.9 dB   |
| Peaking | 2892 Hz  | 3.56 | -14.2 dB |
| Peaking | 3621 Hz  | 1.45 | 6.4 dB   |
| Peaking | 6326 Hz  | 7.2  | 5.3 dB   |
| Peaking | 18699 Hz | 2.09 | -4.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20QZ900/Koss%20QZ900.png)
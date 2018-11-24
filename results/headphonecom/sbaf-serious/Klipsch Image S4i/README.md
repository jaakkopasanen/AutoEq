# Klipsch Image S4i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 21 -8.7; 23 -8.7; 25 -8.7; 28 -8.8; 31 -8.8; 34 -8.8; 37 -8.8; 41 -8.8; 45 -8.9; 49 -9.1; 54 -9.3; 60 -9.4; 66 -9.6; 72 -9.8; 79 -10.0; 87 -10.1; 96 -10.3; 106 -10.3; 116 -10.3; 128 -10.4; 141 -10.3; 155 -10.2; 170 -10.0; 187 -9.7; 206 -9.3; 227 -8.9; 249 -8.4; 274 -7.9; 302 -7.1; 332 -6.4; 365 -5.6; 402 -4.9; 442 -4.1; 486 -3.3; 535 -2.5; 588 -1.8; 647 -1.1; 712 -0.4; 783 -0.0; 861 0.1; 947 0.1; 1042 -0.2; 1146 -0.5; 1261 -0.9; 1387 -1.5; 1526 -2.1; 1678 -2.2; 1846 -1.8; 2031 -1.8; 2234 -1.6; 2457 -1.2; 2703 -0.9; 2973 0.1; 3270 2.0; 3597 3.6; 3957 3.2; 4353 1.2; 4788 -0.4; 5267 -1.9; 5793 -4.5; 6373 -3.4; 7010 0.1; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -1.5; 11289 -0.7; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Image S4i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-38**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image S4i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.23 | -8.1 dB |
| Peaking | 132 Hz   | 0.62 | -6.2 dB |
| Peaking | 271 Hz   | 1    | -3.9 dB |
| Peaking | 3775 Hz  | 5.26 | 4.5 dB  |
| Peaking | 5950 Hz  | 5.29 | -5.2 dB |
| Peaking | 922 Hz   | 1.01 | 4.9 dB  |
| Peaking | 1196 Hz  | 0.57 | -4.2 dB |
| Peaking | 3346 Hz  | 4    | 1.8 dB  |
| Peaking | 7331 Hz  | 5.56 | 1.6 dB  |
| Peaking | 10667 Hz | 9.89 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20Image%20S4i/Klipsch%20Image%20S4i.png)
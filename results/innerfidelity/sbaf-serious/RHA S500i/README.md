# RHA S500i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.5dB
GraphicEQ: 21 0.0; 23 3.5; 25 3.1; 28 2.6; 31 2.3; 34 2.0; 37 1.7; 41 1.5; 45 1.2; 49 0.9; 54 0.6; 60 0.1; 66 -0.3; 72 -0.5; 79 -0.9; 87 -1.4; 96 -1.7; 106 -1.9; 116 -2.0; 128 -2.0; 141 -2.4; 155 -2.5; 170 -2.4; 187 -2.3; 206 -2.3; 227 -2.0; 249 -1.9; 274 -1.7; 302 -1.4; 332 -1.2; 365 -0.8; 402 -0.6; 442 -0.2; 486 -0.0; 535 0.3; 588 0.7; 647 0.9; 712 0.8; 783 1.0; 861 0.7; 947 0.3; 1042 -0.3; 1146 -1.0; 1261 -1.6; 1387 -2.6; 1526 -3.6; 1678 -4.5; 1846 -5.0; 2031 -5.7; 2234 -6.8; 2457 -8.2; 2703 -10.3; 2973 -9.1; 3270 -4.4; 3597 -0.7; 3957 0.7; 4353 -0.3; 4788 -0.5; 5267 0.4; 5793 -0.1; 6373 -2.9; 7010 -6.1; 7711 -6.2; 8482 -4.1; 9330 -1.3; 10263 0.0; 11289 0.0; 12418 -1.5; 13660 -3.9; 15026 -2.7; 16529 -0.0; 18182 0.0; 20000 -3.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA S500i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-45**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA S500i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.6  | 4.6 dB  |
| Peaking | 149 Hz   | 0.83 | -2.7 dB |
| Peaking | 2537 Hz  | 1.92 | -9.7 dB |
| Peaking | 13907 Hz | 2.14 | -3.6 dB |
| Peaking | 20036 Hz | 3.2  | -2.5 dB |
| Peaking | 737 Hz   | 2.1  | 1.2 dB  |
| Peaking | 1636 Hz  | 1.82 | -3.8 dB |
| Peaking | 2902 Hz  | 6    | -5.5 dB |
| Peaking | 4379 Hz  | 0.37 | 3.8 dB  |
| Peaking | 7426 Hz  | 2.45 | -9.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20S500i/RHA%20S500i.png)
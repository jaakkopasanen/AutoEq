# Beats Executive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 4.6; 31 2.6; 34 0.7; 37 -0.8; 41 -2.5; 45 -3.9; 49 -5.2; 54 -6.4; 60 -7.6; 66 -8.6; 72 -9.2; 79 -9.9; 87 -10.7; 96 -11.4; 106 -12.0; 116 -12.6; 128 -13.0; 141 -13.3; 155 -13.4; 170 -13.4; 187 -13.2; 206 -12.7; 227 -11.9; 249 -10.8; 274 -9.2; 302 -7.2; 332 -5.0; 365 -2.8; 402 -1.1; 442 -0.3; 486 -0.6; 535 -0.3; 588 -0.1; 647 -0.1; 712 -0.3; 783 -0.1; 861 1.0; 947 0.5; 1042 -0.3; 1146 -1.4; 1261 -1.5; 1387 -3.6; 1526 -4.9; 1678 -5.7; 1846 -6.9; 2031 -7.5; 2234 -7.9; 2457 -8.1; 2703 -8.0; 2973 -8.4; 3270 -10.9; 3597 -7.3; 3957 -2.3; 4353 -4.5; 4788 -7.5; 5267 -3.4; 5793 -1.0; 6373 -1.8; 7010 -2.1; 7711 -5.9; 8482 -8.8; 9330 -9.4; 10263 -6.9; 11289 -1.4; 12418 0.0; 13660 -1.7; 15026 -6.3; 16529 -4.9; 18182 -0.2; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Executive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Executive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-9.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 103 Hz   | 0.9  | -10.9 dB |
| Peaking | 202 Hz   | 1.49 | -9.6 dB  |
| Peaking | 1963 Hz  | 2.16 | -5.9 dB  |
| Peaking | 3156 Hz  | 1.95 | -8.4 dB  |
| Peaking | 9087 Hz  | 2.62 | -9.9 dB  |
| Peaking | 23 Hz    | 2.51 | 8.1 dB   |
| Peaking | 442 Hz   | 4.35 | 2.3 dB   |
| Peaking | 877 Hz   | 2.17 | 1.8 dB   |
| Peaking | 1479 Hz  | 5.41 | -1.6 dB  |
| Peaking | 15744 Hz | 3.92 | -7.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Beats%20Executive/Beats%20Executive.png)
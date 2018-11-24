# Monster Inspiration

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 21 0.0; 23 -0.2; 25 -1.2; 28 -2.6; 31 -3.8; 34 -4.8; 37 -5.6; 41 -6.6; 45 -7.5; 49 -8.3; 54 -9.1; 60 -9.9; 66 -10.6; 72 -11.2; 79 -11.7; 87 -12.1; 96 -12.4; 106 -12.7; 116 -12.8; 128 -12.7; 141 -12.5; 155 -12.2; 170 -11.6; 187 -10.9; 206 -10.0; 227 -9.0; 249 -8.0; 274 -6.9; 302 -5.5; 332 -3.8; 365 -1.9; 402 -0.8; 442 -0.0; 486 1.9; 535 3.6; 588 4.0; 647 3.7; 712 2.9; 783 2.1; 861 1.4; 947 0.6; 1042 -0.3; 1146 -1.2; 1261 -2.4; 1387 -3.7; 1526 -4.6; 1678 -5.7; 1846 -7.2; 2031 -8.5; 2234 -9.7; 2457 -10.9; 2703 -12.3; 2973 -11.9; 3270 -11.3; 3597 -9.7; 3957 -7.5; 4353 -6.4; 4788 -7.4; 5267 -6.3; 5793 -1.8; 6373 3.6; 7010 -0.9; 7711 -5.7; 8482 -8.0; 9330 -7.7; 10263 -6.5; 11289 -5.5; 12418 -7.1; 13660 -10.1; 15026 -10.9; 16529 -9.0; 18182 -3.6; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Inspiration GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Inspiration ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--1.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 80 Hz    | 0.74 | -11.1 dB |
| Peaking | 172 Hz   | 1.37 | -8.0 dB  |
| Peaking | 2828 Hz  | 1.36 | -13.0 dB |
| Peaking | 8958 Hz  | 4.21 | -6.1 dB  |
| Peaking | 14885 Hz | 1.36 | -11.5 dB |
| Peaking | 21 Hz    | 2.99 | 2.4 dB   |
| Peaking | 275 Hz   | 2.83 | -2.7 dB  |
| Peaking | 601 Hz   | 1.73 | 5.7 dB   |
| Peaking | 5742 Hz  | 1.88 | -5.8 dB  |
| Peaking | 6267 Hz  | 5.17 | 13.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Monster%20Inspiration/Monster%20Inspiration.png)
# Massdrop Plus Universal IEM
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 21 -1.7; 23 -1.7; 25 -1.8; 28 -1.9; 31 -2.0; 34 -2.1; 37 -2.2; 41 -2.3; 45 -2.4; 49 -2.5; 54 -2.7; 60 -2.9; 66 -3.1; 72 -3.4; 79 -3.6; 87 -3.9; 96 -4.2; 106 -4.4; 116 -4.5; 128 -4.7; 141 -4.7; 155 -4.7; 170 -4.6; 187 -4.4; 206 -4.2; 227 -3.9; 249 -3.7; 274 -3.3; 302 -2.9; 332 -2.4; 365 -1.9; 402 -1.5; 442 -1.3; 486 -1.0; 535 -0.6; 588 -0.3; 647 0.1; 712 0.4; 783 0.6; 861 0.6; 947 0.3; 1042 -0.2; 1146 -0.9; 1261 -1.5; 1387 -1.8; 1526 -2.2; 1678 -2.4; 1846 -2.6; 2031 -2.5; 2234 -1.9; 2457 -1.0; 2703 -0.1; 2973 0.7; 3270 1.0; 3597 1.0; 3957 0.7; 4353 0.4; 4788 0.7; 5267 1.9; 5793 3.0; 6373 3.2; 7010 1.1; 7711 -1.0; 8482 -1.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -6.6; 15026 -17.1; 16529 -14.7; 18182 -4.6; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop Plus Universal IEM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-33**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop Plus Universal IEM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 44 Hz    | 0.15 | -1.4 dB  |
| Peaking | 183 Hz   | 0.46 | -4.2 dB  |
| Peaking | 1794 Hz  | 1.05 | -5.1 dB  |
| Peaking | 4265 Hz  | 0.07 | 2.8 dB   |
| Peaking | 15687 Hz | 2.23 | -22.1 dB |
| Peaking | 4653 Hz  | 3.89 | -1.9 dB  |
| Peaking | 6381 Hz  | 2.05 | 2.9 dB   |
| Peaking | 7715 Hz  | 3.11 | -4.0 dB  |
| Peaking | 12800 Hz | 3.36 | 5.0 dB   |
| Peaking | 14329 Hz | 5.2  | -5.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Massdrop%20Plus%20Universal%20IEM/Massdrop%20Plus%20Universal%20IEM.png)
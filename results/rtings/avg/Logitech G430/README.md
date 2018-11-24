# Logitech G430

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.6dB
GraphicEQ: 21 0.0; 23 0.7; 25 -0.1; 28 -1.2; 31 -2.1; 34 -2.8; 37 -3.4; 41 -3.9; 45 -4.3; 49 -4.5; 54 -4.6; 60 -4.6; 66 -4.5; 72 -4.3; 79 -4.2; 87 -4.4; 96 -4.6; 106 -4.9; 116 -4.9; 128 -4.6; 141 -4.5; 155 -4.3; 170 -3.9; 187 -3.5; 206 -3.1; 227 -2.6; 249 -2.7; 274 -2.4; 302 -1.3; 332 -0.6; 365 0.2; 402 1.0; 442 1.6; 486 1.3; 535 0.3; 588 -0.4; 647 -0.5; 712 -0.5; 783 -0.4; 861 -0.3; 947 -0.2; 1042 0.1; 1146 -0.0; 1261 0.3; 1387 0.6; 1526 -0.3; 1678 -0.5; 1846 -1.0; 2031 -1.1; 2234 -0.1; 2457 1.7; 2703 2.8; 2973 2.9; 3270 3.2; 3597 4.1; 3957 3.4; 4353 -0.6; 4788 -1.5; 5267 -1.5; 5793 -2.5; 6373 -4.2; 7010 1.2; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.7; 13660 -0.9; 15026 -0.7; 16529 -0.9; 18182 -2.4; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G430 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-45**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G430 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 1.43 | 5.1 dB  |
| Peaking | 71 Hz    | 0.22 | -4.9 dB |
| Peaking | 420 Hz   | 2.12 | 3.3 dB  |
| Peaking | 3386 Hz  | 2.82 | 4.3 dB  |
| Peaking | 6037 Hz  | 4.67 | -4.3 dB |
| Peaking | 2014 Hz  | 2.88 | -4.0 dB |
| Peaking | 2173 Hz  | 1.59 | 2.6 dB  |
| Peaking | 4621 Hz  | 6.93 | -2.3 dB |
| Peaking | 7128 Hz  | 9.94 | 2.4 dB  |
| Peaking | 20116 Hz | 1.61 | -7.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G430/Logitech%20G430.png)
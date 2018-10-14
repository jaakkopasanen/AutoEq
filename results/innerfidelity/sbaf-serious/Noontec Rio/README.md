# Noontec Rio

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 21 -13.9; 23 -13.6; 25 -13.4; 28 -13.1; 31 -12.8; 34 -12.4; 37 -12.1; 41 -11.8; 45 -11.4; 49 -11.1; 54 -10.8; 60 -10.4; 66 -10.1; 72 -9.9; 79 -9.7; 87 -9.5; 96 -9.2; 106 -8.8; 116 -8.5; 128 -8.1; 141 -7.8; 155 -7.4; 170 -6.9; 187 -6.4; 206 -5.9; 227 -5.3; 249 -4.8; 274 -4.3; 302 -3.6; 332 -3.1; 365 -2.5; 402 -2.0; 442 -1.4; 486 -1.1; 535 -0.6; 588 -0.1; 647 0.0; 712 0.7; 783 1.0; 861 0.6; 947 0.3; 1042 -0.2; 1146 -0.5; 1261 -1.0; 1387 -1.8; 1526 -2.7; 1678 -3.4; 1846 -3.8; 2031 -4.1; 2234 -4.8; 2457 -5.5; 2703 -6.6; 2973 -7.1; 3270 -6.4; 3597 -5.3; 3957 -6.9; 4353 -10.8; 4788 -9.3; 5267 -2.1; 5793 3.3; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.5; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.6dB` and instead set Global volume in the UI for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Rio ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.9dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 17 Hz   | 0.18 | -13.6 dB |
| Peaking | 158 Hz  | 0.8  | -3.5 dB  |
| Peaking | 2720 Hz | 1.36 | -6.2 dB  |
| Peaking | 4550 Hz | 3.87 | -10.9 dB |
| Peaking | 6145 Hz | 3.64 | 8.2 dB   |
| Peaking | 303 Hz  | 2.33 | -0.7 dB  |
| Peaking | 790 Hz  | 1.61 | 1.8 dB   |
| Peaking | 1648 Hz | 2.66 | -1.3 dB  |
| Peaking | 2381 Hz | 6.02 | 0.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Rio/Noontec%20Rio.png)
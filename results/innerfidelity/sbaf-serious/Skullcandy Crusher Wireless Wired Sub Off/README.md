# Skullcandy Crusher Wireless Wired Sub Off

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.4dB
GraphicEQ: 21 -4.9; 23 -5.4; 25 -5.7; 28 -6.2; 31 -6.6; 34 -7.0; 37 -7.3; 41 -7.5; 45 -7.5; 49 -7.5; 54 -8.2; 60 -8.0; 66 -6.7; 72 -5.3; 79 -5.9; 87 -8.3; 96 -9.3; 106 -9.0; 116 -9.4; 128 -10.6; 141 -10.9; 155 -9.9; 170 -9.5; 187 -9.3; 206 -8.2; 227 -6.8; 249 -5.5; 274 -4.2; 302 -2.9; 332 -2.1; 365 -0.9; 402 -0.1; 442 0.7; 486 1.1; 535 1.5; 588 2.3; 647 1.4; 712 0.2; 783 -0.3; 861 -0.2; 947 -0.0; 1042 -0.0; 1146 0.1; 1261 0.4; 1387 -0.0; 1526 -0.7; 1678 -1.3; 1846 -1.8; 2031 -2.1; 2234 -2.9; 2457 -3.1; 2703 -3.9; 2973 -4.7; 3270 -4.7; 3597 -4.1; 3957 -3.6; 4353 -4.4; 4788 -2.8; 5267 -0.8; 5793 -3.7; 6373 -3.6; 7010 -4.1; 7711 -5.6; 8482 -7.6; 9330 -8.8; 10263 -8.5; 11289 -6.9; 12418 -4.8; 13660 -1.9; 15026 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.4dB` and instead set Global volume in the UI for both channels to **-23**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Crusher Wireless Wired Sub Off ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of --0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.48 | -6.8 dB |
| Peaking | 151 Hz   | 1.19 | -9.1 dB |
| Peaking | 3144 Hz  | 1.5  | -4.4 dB |
| Peaking | 9660 Hz  | 1.55 | -9.2 dB |
| Peaking | 75 Hz    | 6.58 | 2.5 dB  |
| Peaking | 91 Hz    | 5.83 | -1.9 dB |
| Peaking | 229 Hz   | 3.62 | -1.7 dB |
| Peaking | 535 Hz   | 1.87 | 2.8 dB  |
| Peaking | 15268 Hz | 3.55 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Crusher%20Wireless%20Wired%20Sub%20Off/Skullcandy%20Crusher%20Wireless%20Wired%20Sub%20Off.png)
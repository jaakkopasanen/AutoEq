# T-Peos U200R

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.4; 23 -5.4; 25 -5.4; 28 -5.4; 31 -5.4; 34 -5.4; 37 -5.4; 41 -5.4; 45 -5.4; 49 -5.4; 54 -5.5; 60 -5.6; 66 -5.7; 72 -5.8; 79 -6.0; 87 -6.2; 96 -6.4; 106 -6.5; 116 -6.4; 128 -6.5; 141 -6.6; 155 -6.5; 170 -6.4; 187 -6.2; 206 -6.0; 227 -5.6; 249 -5.3; 274 -4.9; 302 -4.5; 332 -4.0; 365 -3.5; 402 -3.0; 442 -2.4; 486 -2.0; 535 -1.5; 588 -0.7; 647 -0.2; 712 0.0; 783 0.5; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.5; 1261 -0.7; 1387 -1.4; 1526 -2.2; 1678 -2.7; 1846 -2.7; 2031 -2.3; 2234 -1.3; 2457 1.1; 2703 3.0; 2973 5.4; 3270 6.0; 3597 6.0; 3957 5.0; 4353 0.3; 4788 -4.9; 5267 -2.9; 5793 3.0; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.7; 10263 -0.5; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos U200R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.5dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.2  | -5.3 dB  |
| Peaking | 189 Hz   | 0.73 | -3.9 dB  |
| Peaking | 3572 Hz  | 1.86 | 13.4 dB  |
| Peaking | 5131 Hz  | 1.21 | -24.5 dB |
| Peaking | 5908 Hz  | 1.52 | 20.7 dB  |
| Peaking | 890 Hz   | 1.65 | 1.9 dB   |
| Peaking | 2013 Hz  | 1.3  | -2.6 dB  |
| Peaking | 2693 Hz  | 3.5  | 3.0 dB   |
| Peaking | 9505 Hz  | 5.66 | -2.0 dB  |
| Peaking | 12323 Hz | 1.03 | 1.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20U200R/T-Peos%20U200R.png)
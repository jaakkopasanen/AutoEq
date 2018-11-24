# Jays q-JAY

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.4; 25 3.4; 28 3.2; 31 3.1; 34 3.0; 37 3.0; 41 2.9; 45 2.7; 49 2.6; 54 2.4; 60 2.0; 66 1.7; 72 1.3; 79 1.0; 87 0.5; 96 0.2; 106 -0.1; 116 -0.3; 128 -0.7; 141 -1.0; 155 -1.2; 170 -1.3; 187 -1.4; 206 -1.6; 227 -1.5; 249 -1.5; 274 -1.5; 302 -1.3; 332 -1.3; 365 -1.1; 402 -1.0; 442 -0.6; 486 -0.6; 535 -0.4; 588 0.1; 647 0.3; 712 0.4; 783 0.6; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.2; 1261 -0.4; 1387 -0.8; 1526 -1.1; 1678 -1.1; 1846 -0.6; 2031 -0.1; 2234 0.6; 2457 1.9; 2703 3.3; 2973 5.7; 3270 6.0; 3597 6.0; 3957 5.9; 4353 3.3; 4788 3.9; 5267 5.7; 5793 6.0; 6373 4.7; 7010 2.5; 7711 0.3; 8482 -1.1; 9330 -3.1; 10263 -5.1; 11289 -3.5; 12418 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jays q-JAY GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jays q-JAY ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.37 | 3.5 dB  |
| Peaking | 48 Hz    | 2.15 | 2.1 dB  |
| Peaking | 3385 Hz  | 2.63 | 6.3 dB  |
| Peaking | 5770 Hz  | 2.59 | 5.9 dB  |
| Peaking | 10191 Hz | 3.14 | -5.9 dB |
| Peaking | 70 Hz    | 2.53 | 0.8 dB  |
| Peaking | 215 Hz   | 0.92 | -1.8 dB |
| Peaking | 1675 Hz  | 2.71 | -1.7 dB |
| Peaking | 2896 Hz  | 7.72 | 1.2 dB  |
| Peaking | 12603 Hz | 7.1  | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Jays%20q-JAY/Jays%20q-JAY.png)
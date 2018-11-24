# Fostex T50RP 2011 A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 5.7; 116 5.0; 128 4.1; 141 3.4; 155 3.0; 170 2.6; 187 2.1; 206 1.8; 227 1.6; 249 1.4; 274 1.6; 302 1.8; 332 2.2; 365 2.1; 402 1.9; 442 1.8; 486 1.5; 535 1.7; 588 2.1; 647 1.6; 712 1.4; 783 1.6; 861 0.9; 947 0.2; 1042 0.4; 1146 0.6; 1261 0.7; 1387 0.3; 1526 -0.4; 1678 -0.7; 1846 0.5; 2031 2.2; 2234 3.7; 2457 5.6; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T50RP 2011 A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50RP 2011 A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.33 | 5.9 dB  |
| Peaking | 97 Hz   | 1.23 | 3.0 dB  |
| Peaking | 429 Hz  | 1.26 | 1.6 dB  |
| Peaking | 4379 Hz | 0.79 | 7.1 dB  |
| Peaking | 8670 Hz | 1.91 | -2.9 dB |
| Peaking | 1578 Hz | 4.14 | -1.0 dB |
| Peaking | 1755 Hz | 2.81 | -2.1 dB |
| Peaking | 2601 Hz | 2.32 | 3.0 dB  |
| Peaking | 4715 Hz | 0.86 | -1.4 dB |
| Peaking | 6044 Hz | 4.13 | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T50RP%202011%20A/Fostex%20T50RP%202011%20A.png)
# Enigmatic Audio Paradox

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.8; 25 3.5; 28 3.1; 31 2.9; 34 2.7; 37 2.5; 41 2.4; 45 2.4; 49 2.3; 54 2.1; 60 1.4; 66 1.2; 72 1.1; 79 1.1; 87 0.8; 96 -0.2; 106 -1.7; 116 -2.7; 128 -3.3; 141 -3.5; 155 -3.3; 170 -3.1; 187 -3.9; 206 -3.8; 227 -3.7; 249 -3.5; 274 -3.2; 302 -2.8; 332 -2.3; 365 -0.4; 402 0.2; 442 0.6; 486 0.7; 535 0.7; 588 1.1; 647 2.3; 712 2.0; 783 1.8; 861 1.4; 947 0.5; 1042 -0.3; 1146 -0.4; 1261 -0.3; 1387 -0.3; 1526 -0.0; 1678 0.7; 1846 1.2; 2031 2.5; 2234 3.7; 2457 5.0; 2703 5.9; 2973 6.0; 3270 5.7; 3597 4.6; 3957 4.3; 4353 4.3; 4788 5.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.8; 9330 -2.3; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Enigmatic Audio Paradox GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Enigmatic Audio Paradox ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.14 | 3.7 dB  |
| Peaking | 173 Hz  | 0.64 | -5.8 dB |
| Peaking | 586 Hz  | 1.45 | 2.7 dB  |
| Peaking | 2912 Hz | 1.93 | 6.0 dB  |
| Peaking | 5463 Hz | 2.56 | 6.1 dB  |
| Peaking | 39 Hz   | 2.49 | -0.3 dB |
| Peaking | 807 Hz  | 3.68 | 1.0 dB  |
| Peaking | 1205 Hz | 2.2  | -1.3 dB |
| Peaking | 6460 Hz | 9.5  | 2.0 dB  |
| Peaking | 8987 Hz | 4.94 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Enigmatic%20Audio%20Paradox/Enigmatic%20Audio%20Paradox.png)
# Monster Lady Gaga
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.8dB
GraphicEQ: 21 -4.7; 23 -4.9; 25 -5.1; 28 -5.3; 31 -5.3; 34 -5.4; 37 -5.4; 41 -5.3; 45 -5.2; 49 -5.2; 54 -5.2; 60 -5.1; 66 -5.1; 72 -5.1; 79 -5.1; 87 -5.0; 96 -5.1; 106 -4.8; 116 -4.7; 128 -4.6; 141 -4.4; 155 -4.2; 170 -3.8; 187 -3.5; 206 -3.2; 227 -2.7; 249 -2.5; 274 -2.0; 302 -1.6; 332 -1.3; 365 -0.9; 402 -0.6; 442 -0.1; 486 -0.1; 535 0.3; 588 0.8; 647 0.9; 712 0.9; 783 1.0; 861 0.7; 947 0.3; 1042 -0.2; 1146 -0.6; 1261 -1.1; 1387 -1.9; 1526 -2.7; 1678 -3.4; 1846 -3.6; 2031 -3.6; 2234 -3.6; 2457 -3.1; 2703 -2.3; 2973 -0.6; 3270 1.3; 3597 1.9; 3957 1.1; 4353 -1.0; 4788 -1.3; 5267 0.5; 5793 2.5; 6373 3.6; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.4; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Lady Gaga GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-37**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Lady Gaga ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 0.27 | -5.6 dB |
| Peaking | 2063 Hz | 1.76 | -4.3 dB |
| Peaking | 3563 Hz | 3.84 | 3.3 dB  |
| Peaking | 4564 Hz | 4.5  | -2.2 dB |
| Peaking | 6304 Hz | 4.12 | 4.2 dB  |
| Peaking | 62 Hz   | 1.77 | 0.6 dB  |
| Peaking | 176 Hz  | 1.02 | -0.7 dB |
| Peaking | 683 Hz  | 1.2  | 1.7 dB  |
| Peaking | 1514 Hz | 3.76 | -1.1 dB |
| Peaking | 9085 Hz | 3.66 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Lady%20Gaga/Monster%20Lady%20Gaga.png)
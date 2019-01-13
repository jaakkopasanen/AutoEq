# Oppo PM3 sample A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.8; 25 0.8; 28 0.8; 31 0.8; 34 0.8; 37 0.8; 41 0.8; 45 0.9; 49 0.9; 54 0.9; 60 0.9; 66 0.9; 72 0.8; 79 0.7; 87 0.6; 96 0.2; 106 0.2; 116 0.4; 128 0.6; 141 0.5; 155 -0.0; 170 1.1; 187 0.8; 206 0.6; 227 0.9; 249 1.5; 274 2.1; 302 2.5; 332 2.6; 365 2.4; 402 2.2; 442 1.9; 486 1.3; 535 1.0; 588 0.9; 647 0.8; 712 0.5; 783 0.6; 861 0.5; 947 0.3; 1042 -0.1; 1146 -0.3; 1261 -0.4; 1387 -1.1; 1526 -1.8; 1678 -2.9; 1846 -3.7; 2031 -3.1; 2234 -3.1; 2457 -2.4; 2703 -1.3; 2973 0.3; 3270 0.9; 3597 1.1; 3957 2.0; 4353 1.9; 4788 4.3; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM3 sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.81 | 1.5 dB  |
| Peaking | 37 Hz   | 1.8  | -0.8 dB |
| Peaking | 351 Hz  | 1.23 | 2.6 dB  |
| Peaking | 1960 Hz | 2.12 | -4.1 dB |
| Peaking | 5538 Hz | 2.41 | 6.8 dB  |
| Peaking | 843 Hz  | 3.91 | 0.4 dB  |
| Peaking | 2567 Hz | 4.31 | -1.5 dB |
| Peaking | 3017 Hz | 1.98 | 1.2 dB  |
| Peaking | 6556 Hz | 5.59 | 3.2 dB  |
| Peaking | 7149 Hz | 1.84 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM3%20sample%20A/Oppo%20PM3%20sample%20A.png)
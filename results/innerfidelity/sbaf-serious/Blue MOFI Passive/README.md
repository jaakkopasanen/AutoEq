# Blue MOFI Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.4; 25 1.3; 28 1.2; 31 1.1; 34 1.1; 37 1.0; 41 0.9; 45 0.9; 49 0.8; 54 0.7; 60 0.6; 66 0.4; 72 0.2; 79 -0.1; 87 -0.3; 96 -0.8; 106 -0.9; 116 -0.8; 128 -0.9; 141 -1.6; 155 -1.9; 170 -1.1; 187 -1.6; 206 -1.7; 227 -1.1; 249 -0.5; 274 0.6; 302 1.5; 332 1.8; 365 1.5; 402 1.5; 442 2.9; 486 3.3; 535 2.7; 588 2.6; 647 2.5; 712 1.7; 783 1.4; 861 1.0; 947 0.2; 1042 -0.1; 1146 -0.1; 1261 -0.1; 1387 -0.2; 1526 -0.6; 1678 -0.6; 1846 -0.0; 2031 1.3; 2234 2.1; 2457 2.5; 2703 3.8; 2973 4.4; 3270 4.7; 3597 5.9; 3957 4.3; 4353 1.1; 4788 5.6; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Blue MOFI Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Blue MOFI Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 189 Hz  | 1.16 | -2.1 dB |
| Peaking | 307 Hz  | 3.44 | 1.9 dB  |
| Peaking | 515 Hz  | 1.83 | 3.4 dB  |
| Peaking | 3265 Hz | 2.29 | 5.0 dB  |
| Peaking | 5670 Hz | 2.96 | 6.2 dB  |
| Peaking | 22 Hz   | 1.13 | 1.5 dB  |
| Peaking | 47 Hz   | 2.26 | 0.6 dB  |
| Peaking | 1708 Hz | 2.04 | -1.7 dB |
| Peaking | 2177 Hz | 2.66 | 1.5 dB  |
| Peaking | 8290 Hz | 4.64 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Blue%20MOFI%20Passive/Blue%20MOFI%20Passive.png)
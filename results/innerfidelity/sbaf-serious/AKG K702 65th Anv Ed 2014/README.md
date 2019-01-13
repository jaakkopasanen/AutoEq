# AKG K702 65th Anv Ed 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 21 0.0; 23 2.4; 25 1.9; 28 1.3; 31 0.8; 34 0.4; 37 0.1; 41 -0.3; 45 -0.6; 49 -0.9; 54 -1.2; 60 -1.6; 66 -1.8; 72 -2.2; 79 -2.5; 87 -2.9; 96 -3.3; 106 -3.5; 116 -3.7; 128 -3.8; 141 -4.0; 155 -4.5; 170 -4.3; 187 -4.2; 206 -4.5; 227 -4.7; 249 -4.7; 274 -4.7; 302 -4.6; 332 -4.5; 365 -4.3; 402 -4.2; 442 -3.8; 486 -3.5; 535 -3.1; 588 -2.4; 647 -2.1; 712 -1.5; 783 -0.7; 861 -0.4; 947 -0.1; 1042 0.0; 1146 0.3; 1261 0.6; 1387 -0.3; 1526 -2.1; 1678 -3.4; 1846 -4.1; 2031 -4.3; 2234 -3.1; 2457 -0.0; 2703 3.1; 2973 4.8; 3270 4.9; 3597 3.8; 3957 1.5; 4353 -1.1; 4788 -0.9; 5267 -0.6; 5793 -2.9; 6373 -4.1; 7010 -5.5; 7711 -4.9; 8482 -4.3; 9330 -1.7; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.8; 18182 -3.5; 20000 -2.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K702 65th Anv Ed 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-51**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K702 65th Anv Ed 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 21 Hz    |  1.49 | 3.3 dB  |
| Peaking | 209 Hz   |  0.45 | -4.9 dB |
| Peaking | 2008 Hz  |  3.08 | -5.6 dB |
| Peaking | 3106 Hz  |  2.54 | 6.5 dB  |
| Peaking | 7147 Hz  |  2.04 | -5.8 dB |
| Peaking | 1206 Hz  |  2.11 | 1.7 dB  |
| Peaking | 1611 Hz  |  5.39 | -1.8 dB |
| Peaking | 4373 Hz  | 10.47 | -1.7 dB |
| Peaking | 15168 Hz |  0.88 | 2.4 dB  |
| Peaking | 18142 Hz |  1.04 | -4.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K702%2065th%20Anv%20Ed%202014/AKG%20K702%2065th%20Anv%20Ed%202014.png)